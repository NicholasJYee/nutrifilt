! f2py terminal compile line
! f2py -c -m sim_anneal  meals/simulated_annealing.f90
SUBROUTINE sim_anneal(TEMPERATURE_INI, &
    meal_types, plan, nutrition_req, breakfast, snack, lunch, dinner, &
    plan_size, nutrition_req_size, breakfast_size, snack_size, lunch_size, dinner_size)
  IMPLICIT NONE
  INTEGER, INTENT(IN) :: plan_size, nutrition_req_size, breakfast_size, snack_size, lunch_size, dinner_size
  REAL(8), DIMENSION(nutrition_req_size), INTENT(IN) :: nutrition_req
  REAL(8), DIMENSION(breakfast_size, 32), INTENT(IN) :: breakfast
  REAL(8), DIMENSION(snack_size, 32), INTENT(IN) :: snack
  REAL(8), DIMENSION(lunch_size, 32), INTENT(IN) :: lunch
  REAL(8), DIMENSION(dinner_size, 32), INTENT(IN) :: dinner
  REAL(8), DIMENSION(plan_size, 32), INTENT(INOUT) :: plan
  REAL(8), DIMENSION(plan_size, 32), INTENT(IN) :: meal_types
  REAL(8), DIMENSION(plan_size, 32) :: cheapest_plan, new_plan
  REAL(8), INTENT(IN) :: TEMPERATURE_INI
  REAL(8) :: TEMPERATURE_END
  REAL(8) :: temperature
  REAL(8) :: plan_cost, total_cost, lowest_cost, previous_cost
  REAL(8) :: accept_probability, rand_accept
  INTEGER :: num_of_reinitialize
  INTEGER :: TEMPERATURE_NUMB_STEP, DRAWS
  INTEGER :: k, j

  TEMPERATURE_END = 0.01d0
  IF (TEMPERATURE_INI .EQ. 1.d0) THEN
    WRITE(*,*) "Cheapest"
    TEMPERATURE_NUMB_STEP = 20
    DRAWS = 500000  
  ELSE IF (TEMPERATURE_INI .EQ. 5.5d0) THEN
    WRITE(*,*) "Cheap"
    TEMPERATURE_NUMB_STEP = 10
    DRAWS = 100000  
  ELSE IF (TEMPERATURE_INI .EQ. 10.d0) THEN
    WRITE(*,*) "Normal"
    TEMPERATURE_NUMB_STEP = 5
    DRAWS = 10000  
  END IF

  temperature = TEMPERATURE_INI
  lowest_cost = plan_cost(plan, plan_size)
  previous_cost = lowest_cost
  cheapest_plan = plan
  num_of_reinitialize = 0

  temperatureSchedule: DO k = 0, TEMPERATURE_NUMB_STEP - 1
    drawSchedule: DO j = 1, DRAWS
      CALL changeOneMeal(num_of_reinitialize, meal_types, plan, new_plan, plan_size, &
        nutrition_req, breakfast, snack, lunch, dinner, &
        nutrition_req_size, breakfast_size, snack_size, lunch_size, dinner_size, j, k, DRAWS, TEMPERATURE_NUMB_STEP)

      total_cost = plan_cost(new_plan, plan_size)
      
      accept_probability = MIN(1.d0, &
        EXP(-(total_cost - previous_cost) / temperature))
      CALL random_number(rand_accept)
      
      determineNewStep: IF (rand_accept .LT. accept_probability) THEN
        plan = new_plan
        previous_cost = total_cost

        checkLowestCost: IF (total_cost .LT. lowest_cost) THEN
          lowest_cost = total_cost
          cheapest_plan = new_plan
        END IF checkLowestCost
      END IF determineNewStep
    END DO drawSchedule
    temperature = temperature - (TEMPERATURE_INI - TEMPERATURE_END) / TEMPERATURE_NUMB_STEP
  END DO temperatureSchedule
  plan = cheapest_plan

END SUBROUTINE

SUBROUTINE changeOneMeal(num_of_reinitialize, meal_types, plan, new_plan, plan_size, &
  nutrition_req, breakfast, snack, lunch, dinner, &
  nutrition_req_size, breakfast_size, snack_size, lunch_size, dinner_size, draw_num, temp_num, DRAWS, TEMPERATURE_NUMB_STEP)
  IMPLICIT NONE
  INTEGER, PARAMETER :: MAX_NUMB_OF_MEAL_PLAN_GENERATED = 5000000
  INTEGER, INTENT(IN) :: plan_size, nutrition_req_size, breakfast_size, snack_size, lunch_size, dinner_size
  INTEGER, INTENT(INOUT) :: temp_num, draw_num
  INTEGER, INTENT(IN) :: TEMPERATURE_NUMB_STEP, DRAWS
  REAL(8), DIMENSION(plan_size, 32), INTENT(IN) :: plan, meal_types
  REAL(8), DIMENSION(plan_size, 32), INTENT(OUT) :: new_plan
  REAL(8), DIMENSION(nutrition_req_size), INTENT(IN) :: nutrition_req
  REAL(8), DIMENSION(breakfast_size, 32), INTENT(IN) :: breakfast
  REAL(8), DIMENSION(snack_size, 32), INTENT(IN) :: snack
  REAL(8), DIMENSION(lunch_size, 32), INTENT(IN) :: lunch
  REAL(8), DIMENSION(dinner_size, 32), INTENT(IN) :: dinner
  INTEGER, INTENT(INOUT) :: num_of_reinitialize
  REAL(8) :: rand_dummy
  INTEGER :: num_of_nutrition_met, nutrition_met
  INTEGER :: which_meal_to_change, new_recipe, num_meals_to_change
  INTEGER :: i, j

  IF (num_of_reinitialize .LT. 3) THEN
    DO i = 1, MAX_NUMB_OF_MEAL_PLAN_GENERATED
      new_plan = plan
      CALL random_number(rand_dummy)
      num_meals_to_change = CEILING((rand_dummy + 0.000001d0) * REAL(plan_size) / 2.d0)
      num_meals_to_change = CEILING(REAL(num_meals_to_change) * (2.d0 - EXP(REAL(temp_num) / (1.5d0 * TEMPERATURE_NUMB_STEP))))

      DO j = 1, num_meals_to_change
        CALL random_number(rand_dummy)
        which_meal_to_change = CEILING((rand_dummy + 0.000001d0) * plan_size)

        CALL random_number(rand_dummy)
        IF (INT(meal_types(which_meal_to_change,1)) .EQ. 1) THEN
          new_recipe = CEILING((rand_dummy + 0.000001d0) * breakfast_size)
          new_plan(which_meal_to_change,:) = breakfast(new_recipe,:)
        ELSE IF (INT(meal_types(which_meal_to_change,1)) .EQ. 2) THEN
          new_recipe = CEILING((rand_dummy + 0.000001d0) * snack_size)
          new_plan(which_meal_to_change,:) = snack(new_recipe,:)
        ELSE IF (INT(meal_types(which_meal_to_change,1)) .EQ. 3) THEN
          new_recipe = CEILING((rand_dummy + 0.000001d0) * lunch_size)
          new_plan(which_meal_to_change,:) = lunch(new_recipe,:)
        ELSE IF (INT(meal_types(which_meal_to_change,1)) .EQ. 4) THEN
          new_recipe = CEILING((rand_dummy + 0.000001d0) * dinner_size)
          new_plan(which_meal_to_change,:) = dinner(new_recipe,:)
        END IF
      END DO

      num_of_nutrition_met = nutrition_met(new_plan, plan_size, nutrition_req, nutrition_req_size)
      IF (num_of_nutrition_met .EQ. nutrition_req_size) THEN
        EXIT
      END IF

      IF (i .EQ. MAX_NUMB_OF_MEAL_PLAN_GENERATED) THEN
        WRITE(*,*) "Couldn't generate another similar plan; new start point"
        CALL generate_plan_meeting_nutrition(&
          new_plan, nutrition_req, breakfast, snack, lunch, dinner, &
          plan_size, nutrition_req_size, breakfast_size, snack_size, lunch_size, dinner_size)
        num_of_reinitialize = num_of_reinitialize + 1
        EXIT
      END IF
    END DO
  ELSE
    WRITE(*,*) "No plan meeting nutritional req :("
    new_plan = plan
    draw_num = DRAWS
    temp_num = TEMPERATURE_NUMB_STEP - 1
  END IF

END SUBROUTINE

REAL(8) FUNCTION plan_cost(plan, plan_size)
  IMPLICIT NONE
  INTEGER, INTENT(IN) :: plan_size  
  REAL(8), DIMENSION(plan_size, 32), INTENT(IN) :: plan
  INTEGER :: i

  plan_cost = 0.d0
  DO i = 1, plan_size
    plan_cost = plan_cost + plan(i,3)
  END DO

END FUNCTION


SUBROUTINE generate_plan_meeting_nutrition(&
    plan, nutrition_req, breakfast, snack, lunch, dinner, &
    plan_size, nutrition_req_size, breakfast_size, snack_size, lunch_size, dinner_size)
  IMPLICIT NONE
  INTEGER, PARAMETER :: MAX_NUMB_OF_MEAL_PLAN_GENERATED = 1000000
  INTEGER, INTENT(IN) :: plan_size, nutrition_req_size, breakfast_size, snack_size, lunch_size, dinner_size
  REAL(8), DIMENSION(nutrition_req_size), INTENT(IN) :: nutrition_req
  REAL(8), DIMENSION(breakfast_size, 32), INTENT(IN) :: breakfast
  REAL(8), DIMENSION(snack_size, 32), INTENT(IN) :: snack
  REAL(8), DIMENSION(lunch_size, 32), INTENT(IN) :: lunch
  REAL(8), DIMENSION(dinner_size, 32), INTENT(IN) :: dinner
  REAL(8), DIMENSION(plan_size, 32), INTENT(INOUT) :: plan
  REAL(8), DIMENSION(plan_size, 32) :: plan_with_most_nutrition
  INTEGER :: i, j, meal_number
  INTEGER :: num_of_nutrition_met, nutrition_met, most_nutrient_met

  most_nutrient_met = 0

  DO i = 1, MAX_NUMB_OF_MEAL_PLAN_GENERATED
    DO j = 1, plan_size
      meal_number = INT(RAND(0) * breakfast_size) + 1
      SELECT CASE (INT(plan(j,1)))
        CASE (1)
          plan(j,:) = breakfast(meal_number,:)
        CASE (2)
          plan(j,:) = snack(meal_number,:)
        CASE (3)
          plan(j,:) = lunch(meal_number,:)
        CASE (4)
          plan(j,:) = dinner(meal_number,:)
      END SELECT
    END DO

    num_of_nutrition_met = nutrition_met(plan, plan_size, nutrition_req, nutrition_req_size)
    IF (num_of_nutrition_met .EQ. nutrition_req_size) THEN
      EXIT
    ELSE IF (num_of_nutrition_met .GT. most_nutrient_met) THEN
      most_nutrient_met = num_of_nutrition_met
      plan_with_most_nutrition = plan
    END IF

    IF (i .EQ. MAX_NUMB_OF_MEAL_PLAN_GENERATED) THEN
      WRITE(*,*) "Cant find plan that met nutrition, but found best plan"
      plan = plan_with_most_nutrition
    END IF
  END DO

END SUBROUTINE generate_plan_meeting_nutrition

INTEGER FUNCTION nutrition_met(plan, plan_size, nutrition_req, nutrition_req_size)
  IMPLICIT NONE
  INTEGER, INTENT(IN) :: plan_size, nutrition_req_size
  REAL(8), DIMENSION(nutrition_req_size), INTENT(IN) :: nutrition_req
  REAL(8), DIMENSION(plan_size, 32), INTENT(IN) :: plan
  REAL(8), DIMENSION(nutrition_req_size) :: meals_nutrition
  INTEGER :: num_of_nutrition_met, i

  num_of_nutrition_met = 0
  CALL get_nutrition(meals_nutrition, plan, plan_size, nutrition_req_size)

  DO i = 1, nutrition_req_size
    IF ((meals_nutrition(i) .GE. (nutrition_req(i) * 0.8d0)) .AND. &
        (meals_nutrition(i) .LE. (nutrition_req(i) * 1.2d0))) THEN
      num_of_nutrition_met = num_of_nutrition_met + 1
    END IF
  END DO
  
  nutrition_met = num_of_nutrition_met
  RETURN
END FUNCTION

SUBROUTINE get_nutrition(meals_nutrition, plan, plan_size, nutrition_req_size)
  IMPLICIT NONE
  INTEGER, INTENT(IN) :: plan_size, nutrition_req_size
  REAL(8), DIMENSION(plan_size, 32), INTENT(IN) :: plan
  REAL(8), DIMENSION(nutrition_req_size), INTENT(OUT) :: meals_nutrition
  INTEGER :: i

  meals_nutrition = 0.d0

  DO i = 1, plan_size
    meals_nutrition(1) = meals_nutrition(1) + plan(i,4)
    meals_nutrition(2) = meals_nutrition(2) + plan(i,5)
    meals_nutrition(3) = meals_nutrition(3) + plan(i,6)
    meals_nutrition(4) = meals_nutrition(4) + plan(i,7)
    meals_nutrition(5) = meals_nutrition(5) + plan(i,8)
    meals_nutrition(6) = meals_nutrition(6) + plan(i,9)
    meals_nutrition(7) = meals_nutrition(7) + plan(i,10)
    meals_nutrition(8) = meals_nutrition(8) + plan(i,11)
    meals_nutrition(9) = meals_nutrition(9) + plan(i,12)
    meals_nutrition(10) = meals_nutrition(10) + plan(i,13)
    meals_nutrition(11) = meals_nutrition(11) + plan(i,14)
    meals_nutrition(12) = meals_nutrition(12) + plan(i,15)
    meals_nutrition(13) = meals_nutrition(13) + plan(i,16)
    meals_nutrition(14) = meals_nutrition(14) + plan(i,17)
    meals_nutrition(15) = meals_nutrition(15) + plan(i,18)
    meals_nutrition(16) = meals_nutrition(16) + plan(i,19)
    meals_nutrition(17) = meals_nutrition(17) + plan(i,20)
    meals_nutrition(18) = meals_nutrition(18) + plan(i,21)
    meals_nutrition(19) = meals_nutrition(19) + plan(i,22)
    meals_nutrition(20) = meals_nutrition(20) + plan(i,23)
    meals_nutrition(21) = meals_nutrition(21) + plan(i,24)
    meals_nutrition(22) = meals_nutrition(22) + plan(i,25)
    meals_nutrition(23) = meals_nutrition(23) + plan(i,26)
    meals_nutrition(24) = meals_nutrition(24) + plan(i,27)
    meals_nutrition(25) = meals_nutrition(25) + plan(i,28)
    meals_nutrition(26) = meals_nutrition(26) + plan(i,29)
    meals_nutrition(27) = meals_nutrition(27) + plan(i,30)
    meals_nutrition(28) = meals_nutrition(28) + plan(i,31)
    meals_nutrition(29) = meals_nutrition(29) + plan(i,32)
  END DO

END SUBROUTINE

SUBROUTINE get_array(arr1, arr2, row, col)
  IMPLICIT NONE
  INTEGER(8), INTENT(IN) :: row, col
  REAL(8), DIMENSION(row, col), INTENT(INOUT) :: arr1
  REAL(8), DIMENSION(row, col), INTENT(OUT) ::arr2

  WRITE(*,*) "initial arr1: ", arr1
  WRITE(*,*) "pre arr2:", arr2
  arr2 = arr1
  WRITE(*,*) "after assign arr1: ", arr1
  WRITE(*,*) "before change arr2: ", arr2
  arr1(1, 2) = 1.d0
  WRITE(*,*) "post arr2:", arr2
  WRITE(*,*) "post arr1:", arr1

END SUBROUTINE