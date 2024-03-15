from app.controllers.extensions import db
from app.models.personal.users import Level, Business


def CreateLevels():
    level = Level.query.all()

    if not level:
        levels = [
            Level(level='usr'),
            Level(level='pat'),
            Level(level='adm')
        ]

        db.session.add_all(levels)
        db.session.commit()

    return not bool(level)


def CreateBusiness():
    business = Business.query.all()

    if not business:
        businesses = [
            Business(function='doctor'),
            Business(function='developer'),
            Business(function='hr'),
            Business(function='assistant')
        ]

        db.session.add_all(businesses)
        db.session.commit()

    return not bool(business)
