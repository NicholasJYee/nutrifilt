SUBROUTINE generate_plan_meeting_nutrition(&
    plan, nutrition_req, breakfast, snack, lunch, dinner, &
    plan_size, nutrition_req_size, breakfast_size, snack_size, lunch_size, dinner_size)
  IMPLICIT NONE
  INTEGER, PARAMETER :: MAX_NUMB_OF_INITIAL_MEAL_PLAN_GENERATED = 500000
  INTEGER, INTENT(IN) :: plan_size, nutrition_req_size, breakfast_size, snack_size, lunch_size, dinner_size
  REAL(8), DIMENSION(nutrition_req_size), INTENT(IN) :: nutrition_req
  REAL(8), DIMENSION(breakfast_size, 32), INTENT(IN) :: breakfast
  REAL(8), DIMENSION(snack_size, 32), INTENT(IN) :: snack
  REAL(8), DIMENSION(lunch_size, 32), INTENT(IN) :: lunch
  REAL(8), DIMENSION(dinner_size, 32), INTENT(IN) :: dinner
  REAL(8), DIMENSION(plan_size, 32), INTENT(INOUT) :: plan
  INTEGER :: i, j, meal_number
  LOGICAL :: met_nutrient_requirement, nutrition_met

  DO i = 1, MAX_NUMB_OF_INITIAL_MEAL_PLAN_GENERATED
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

    met_nutrient_requirement = nutrition_met(plan, plan_size, nutrition_req, nutrition_req_size)
    IF (met_nutrient_requirement) THEN
      EXIT
    END IF
  END DO

END SUBROUTINE generate_plan_meeting_nutrition

LOGICAL FUNCTION nutrition_met(plan, plan_size, nutrition_req, nutrition_req_size)
  IMPLICIT NONE
  INTEGER, INTENT(IN) :: plan_size, nutrition_req_size
  REAL(8), DIMENSION(nutrition_req_size), INTENT(IN) :: nutrition_req
  REAL(8), DIMENSION(plan_size, 32), INTENT(IN) :: plan
  REAL(8), DIMENSION(nutrition_req_size) :: meals_nutrition
  INTEGER :: num_of_nutrition_met

  num_of_nutrition_met = 0
  CALL get_nutrition(meals_nutrition, plan, plan_size, nutrition_req_size)

  nutrition_met = .TRUE.

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

SUBROUTINE get_array(arr, row, col)
  IMPLICIT NONE
  INTEGER(8), INTENT(IN) :: row, col
  REAL(8), DIMENSION(row, col), INTENT(INOUT) :: arr

  arr(1, 2) = 1.d0

END SUBROUTINE