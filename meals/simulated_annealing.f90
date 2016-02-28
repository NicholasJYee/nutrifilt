SUBROUTINE generate_plan_meeting_nutrition(plan, &
    breakfast, snack, lunch, dinner, breakfast_size, snack_size, lunch_size, dinner_size)
  IMPLICIT NONE
  INTEGER, INTENT(IN) :: breakfast_size, snack_size, lunch_size, dinner_size
  REAL(8), DIMENSION(breakfast_size, 31), INTENT(IN) :: breakfast
  REAL(8), DIMENSION(snack_size, 31), INTENT(IN) :: snack
  REAL(8), DIMENSION(lunch_size, 31), INTENT(IN) :: lunch
  REAL(8), DIMENSION(dinner_size, 31), INTENT(IN) :: dinner
  REAL(8), DIMENSION(5, 31), INTENT(OUT) :: plan



END SUBROUTINE generate_plan_meeting_nutrition

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