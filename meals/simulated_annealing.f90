SUBROUTINE generate_plan_meeting_nutrition(max_size, meals, nutrition_req, selected_meals)
  IMPLICIT NONE
  INTEGER, INTENT(IN) :: max_size
  REAL, DIMENSION(5, max_size), INTENT(IN) :: meals
  REAL, DIMENSION(5), INTENT(OUT) :: selected_meals
  REAL, DIMENSION(29), INTENT(IN) :: nutrition_req
  INTEGER :: tries, i
  REAL :: randNum
  INTEGER, PARAMETER :: MAX_NUMB_OF_INITIAL_MEAL_PLAN_GENERATED = 500000
  PRINT*, MAX_NUMB_OF_INITIAL_MEAL_PLAN_GENERATED

  ! DO tries = 0, MAX_NUMB_OF_INITIAL_MEAL_PLAN_GENERATED
  !   DO i = 1, SIZE(meals)
  !     CALL random_number(randNum)
  !     selected_meals(i) = meals(i, INT(randNum * SIZE(meals(i, :))) + 1)
  !   END DO

  ! END DO 


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