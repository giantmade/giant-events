## 0.2.6
- Fix admin search on foreign key field (location).

## 0.2.5
- Use `timezone.now()` instead of `Now()` when evaluating past/future querysets
- Update the past/future filtering conditions so events aren't moved prematurely.

## 0.1.2
- Combine author name fields into one
- Add Category model
- Update url to be more explicit
- Add str test for new model

## 0.1.2.1
- add read time

## 0.1.2.2
- Change URL property on Article model to a method to remove error when using "view on site" 