Django에서 폼을 작성할 때, `{{ form.as_p }}`와 같은 방식으로 자동으로 렌더링하면 Django는 기본적으로 각 필드를 `<p>` 태그로 감싸서 출력합니다. 이 방식은 **HTML 요소를 직접 조정하거나 스타일을 적용할 수 없는** 단점이 있습니다. 그러나 **부트스트랩**을 사용하여 폼을 스타일링하려면, 필드별로 직접 CSS 클래스를 추가하거나 커스터마이징된 템플릿을 작성하는 것이 필요합니다.

### 1. `{{ form.as_p }}` 사용 시 부트스트랩 적용
`{{ form.as_p }}`는 Django 폼을 `<p>` 태그로 감싸 출력하지만, 부트스트랩 클래스는 적용되지 않습니다. 따라서 부트스트랩 스타일을 적용하려면 다음 방법을 사용할 수 있습니다.

#### 예시 1: 필드별로 직접 클래스 추가
폼 필드를 하나씩 렌더링하여 각 필드에 부트스트랩 클래스를 수동으로 추가할 수 있습니다.

```html
<form method="post">
    {% csrf_token %}
    <div class="form-group">
        <label for="title">Title</label>
        <input type="text" id="title" name="title" value="{{ article.title }}" class="form-control">
    </div>

    <div class="form-group">
        <label for="content">Content</label>
        <textarea id="content" name="content" class="form-control">{{ article.content }}</textarea>
    </div>

    <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

이 방식은 각 입력 필드에 `form-control` 클래스를 적용하여 부트스트랩 스타일을 적용하는 방법입니다.

#### 예시 2: `{{ form.as_p }}`와 부트스트랩 클래스를 결합
Django 폼을 `{{ form.as_p }}`로 렌더링하고, 각 필드에 **부트스트랩** 클래스를 자동으로 적용하려면, 폼 위젯을 수정해야 합니다. 예를 들어, Django 폼에서 `widgets`를 사용하여 필드에 부트스트랩 클래스를 적용할 수 있습니다.

### 2. 폼 위젯을 수정하여 부트스트랩 스타일 적용

Django 폼에서 각 입력 필드에 부트스트랩 클래스를 적용하려면, **폼 클래스의 `widgets` 속성**을 활용해야 합니다. 예를 들어, `forms.py`에서 폼을 정의할 때 위젯에 부트스트랩 클래스를 지정할 수 있습니다.

#### 예시: `forms.py`에서 부트스트랩 클래스 추가

```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
    
    # 위젯에 부트스트랩 클래스를 추가
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
```

위의 코드에서는 `ArticleForm` 폼 클래스에서 **모든 필드에 `form-control` 클래스를 자동으로 추가**합니다. 이렇게 하면, `{{ form.as_p }}`를 사용하더라도 각 입력 필드에 부트스트랩 스타일이 적용됩니다.

#### 3. 템플릿에서 폼 렌더링

이제 `{{ form.as_p }}`를 템플릿에서 사용하면, 모든 입력 필드에 부트스트랩 클래스가 자동으로 적용됩니다.

```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

이 방식으로 부트스트랩을 사용하면 각 필드가 `form-control` 클래스를 가지게 되어, 부트스트랩 스타일이 자동으로 적용됩니다.

### 4. 커스터마이즈된 폼 렌더링

필요한 경우 각 폼 필드를 개별적으로 커스터마이즈할 수도 있습니다. 예를 들어, `{{ form.title }}`와 같은 방식으로 필드별로 직접 렌더링하고, 각 필드에 부트스트랩 클래스를 추가하는 방법입니다.

```html
<form method="post">
    {% csrf_token %}
    <div class="form-group">
        {{ form.title }}
    </div>
    <div class="form-group">
        {{ form.content }}
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

이 방식은 각 필드에 대해 더 세밀하게 제어할 수 있고, 필요에 따라 특정 필드에 추가적인 클래스를 적용할 수도 있습니다.

### 결론
- `{{ form.as_p }}`는 부트스트랩 스타일을 직접 적용하기 어렵기 때문에, 각 필드를 수동으로 렌더링하거나 `widgets` 속성을 사용하여 부트스트랩 클래스를 자동으로 적용하는 방법이 있습니다.
- `forms.py`에서 **`widgets`**나 **`__init__` 메서드를 활용**해 폼 필드에 부트스트랩 스타일을 추가하는 것이 가장 효율적입니다.