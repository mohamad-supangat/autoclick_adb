import random
from autoclick import helpers, db
from autoclick.helpers import device, tap, random_sleep


total_like = 0
total_comment = 0


def search_like_button():
    return device(
        descriptionContains='Like video', className='android.widget.Button'
    )


def scroll_page():
    return helpers.device.swipe(292, 1050, 292, 163, 0.1)


def close_comment():
    close_comment = device(descriptionContains='Close comments')
    if close_comment:
        position = close_comment.center()
        tap(position[0], position[1])


def auto_comment():
    global total_comment
    random_sleep()

    has_comment_button = device(
        className='android.widget.Button',
        descriptionContains='Read or add comments',
    )
    # klik tombol komentar
    if has_comment_button:
        position = has_comment_button.center()
        tap(position[0], position[1])
        random_sleep()
        has_comment_input = device(
            className='android.widget.EditText', textContains='Add comment'
        )
        if has_comment_input:
            position = has_comment_input.center()
            tap(position[0], position[1])
            tap(position[0], position[1])

            comment_text = random.choice(db.comments)
            print(f'comment: {comment_text}')
            has_comment_input.set_text(comment_text)
            random_sleep()

            submit_button = device(
                className='android.widget.ImageView',
                descriptionContains='Post comment',
            ).center()
            tap(submit_button[0], submit_button[1])
            total_comment += 1
            random_sleep()


while True:
    if random.randint(1, 999) % 2 == 1:
        continue

    random_sleep()
    has_like_button = search_like_button()
    if has_like_button:
        position = has_like_button.center()
        tap(x=position[0], y=position[1])
        print('Like')
        total_like += 1
        if random.randint(1, 999) % 2 == 1:
            auto_comment()

    close_comment()
    random_sleep()
    print(f'like: {total_like}')
    print(f'comment: {total_comment}')

    scroll_page()
