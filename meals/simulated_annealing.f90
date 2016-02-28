SUBROUTINE generate_plan_meeting_nutrition(&
    plan, nutrition_req, breakfast, snack, lunch, dinner, &
    plan_size, nutrition_req_size, breakfast_size, snack_size, lunch_size, dinner_size)
  IMPLICIT NONE
  INTEGER, PARAMETER :: MAX_NUMB_OF_INITIAL_MEAL_PLAN_GENERATED = 500000
  INTEGER, INTENT(IN) :: plan_size, nutrition_req_size, breakfast_size, snack_size, lunch_size, dinner_size
  REAL(8), DIMENSION(nutrition_req_size), INTENT(IN) :: nutrition_req
  REAL(8), DIMENSION(breakfast_size, 31), INTENT(IN) :: breakfast
  REAL(8), DIMENSION(snack_size, 31), INTENT(IN) :: snack
  REAL(8), DIMENSION(lunch_size, 31), INTENT(IN) :: lunch
  REAL(8), DIMENSION(dinner_size, 31), INTENT(IN) :: dinner
  REAL(8), DIMENSION(plan_size, 31), INTENT(INOUT) :: plan
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

    met_nutrient_requirement = nutrition_met(plan, nutrition_req)
    IF (met_nutrient_requirement) THEN
      plan = 1.d0
    ELSE 
      plan = 2.d0
    END IF
  END DO

END SUBROUTINE generate_plan_meeting_nutrition

LOGICAL FUNCTION nutrition_met(plan, plan_size, nutrition_req, nutrition_req_size)
  IMPLICIT NONE
  INTEGER, INTENT(IN) :: plan_size, nutrition_req_size
  REAL(8), DIMENSION(nutrition_req_size), INTENT(IN) :: nutrition_req
  REAL(8), DIMENSION(plan_size, 31), INTENT(IN) :: plan

  nutrition_met = .FALSE.

END FUNCTION

SUBROUTINE get_array(arr, row, col)
  IMPLICIT NONE
  INTEGER(8), INTENT(IN) :: row, col
  REAL(8), DIMENSION(row, col), INTENT(INOUT) :: arr

  arr(1, 2) = 1.d0

END SUBROUTINE

! def generate_plan_meeting_nutrition(meals, nutrition_req):
!   tries = 0
!   while True:
!     selected_meals = []
!     tries += 1

!     for i, meal in enumerate(meals):
!       selected_meals.append(choice(meals[i]))

!     met_nutrient_requirement = nutrition_met(selected_meals, nutrition_req)
!     if met_nutrient_requirement:
!       break

!     if tries == MAX_NUMB_OF_INITIAL_MEAL_PLAN_GENERATED:
!       break

!   return selected_meals