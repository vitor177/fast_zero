from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    # Registry cria a tabela a partir dos metadados

    user = User(username='joao2', email='joaovito2r@gmail.com', password='123')

    session.add(user)
    session.commit()
    session.refresh(user)

    result = session.scalar(
        select(User).where(User.email == 'joaovito2r@gmail.com')
    )

    assert user.id == 1
    assert result.username == 'joao2'
