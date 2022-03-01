DependencyIngection (feat.spring)
DependencyIngection (feat.spring)

이 글은 스프링에서 주입되는 방법에 대해 적어보도록 하겠다.

스프링에 객체에 주입하는 방법은 4가지가 존재한다 .

1. [생성자 주입](#생성자-주입)
2. [필드 주입](#필드-주입)
3. [메서드 주입](#메서드-주입)
4. [수정자 주입](#수정자-주입)

## 생성자 주입
생성자를 통해 주입을 하는 방식이다.

	@Component  
	public class MemberServiceImpl implements MemberService{  
	   
	  private final MemberRepository repository;  
	  
	  @Autowired  
	  public MemberServiceImpl(MemberRepository repository) {  
	        this.repository = repository;  
	  }
	}

생성자를 통해 주입하는 방식이다.  생성자 위에 있는 @Autowired는 제거 해도 상관없다. class의 생성자가 1개만 존재한다면 자동으로 주입을 해준다. (스프링 빈일때만 그런 것이다. 프레임워크를 다른 것을 사용하는 사람은 참조 바란다.)

## 필드 주입

	@Component  
		public class MemberServiceImpl implements 
		MemberService{  
	  
	  @Autowired   
	  private final MemberRepository repository;  
	  
	}

필드에 @Autowired를 통해 객체를 주입해준다. 개인적으로는 필드 주입 방식을 많이 봤던 것 같다.

## 메서드 주입

	@Component  
		public class MemberServiceImpl implements 
		MemberService{  
	  
	  private final MemberRepository repository;  
	  
	  public void init(MemoryMemberRepository memoryMemberRepository)
	  this.repository = memoryMemberRepository;
	}

일단 메서드를 통해 객체를 주입하는 방식.

## 수정자 주입

	@Component  
		public class MemberServiceImpl implements 
		MemberService{  
	     
	  private final MemberRepository repository;  
	  
	  public void setter(MemoryMemberRepository memoryMemberRepository) {
			this.repository = memoryMemberRepository;
		}
	}

setter 수정자를 제공하여 객체를 주입하는 방식이다.


이렇게 4가지의 주입방식을 살펴보았다.
그리고 내가 하고 싶은 말은 "어떤 것을 어떨 때 사용해야 좋을까 ?!" 이다.

개발을 하면서 하나가 무조건 좋다고 말할 수 없다. 적재적소가 필요하다.

하지만 DI의 경우 -> 많은 사람들(필자가 수강했던 강의 강사, DI와 관련된 포스팅, 스프링 공식문서)이 생성자 주입을 많이 사용하고 ,
사용하도록 권고한다.

위 의견에 동의하는 바이다.
테스트와 관련하여 생성자 주입이 꽤 도움이 된다. 우선 스프링 등록된 빈을 이용해 주입을 해줘야 한다면 @SpringBootTest -> 을 통해서 스프링 기동이 필요할 수 있다. 이러면 꽤 오랜 시간을 잡아 먹을 수 있다.

때문에 생성자를 통해 원하는 객체를 직접 초기화하여 테스트할 수 있기 때문에 생성자 주입을 주로 사용할 것이다. 그렇게 습관을 형성하고 있다.

역시 이것도 상황에 적절하지 못하다면 사용하지 않는 것이 좋을 수 있다.
그리고 나의 포스팅은 30%만 신뢰하길 바란다.

나도 나를 의심하면서 글을 작성합니다.


> Written with [StackEdit](https://stackedit.io/).
이 글은 스프링에서 주입되는 방법에 대해 적어보도록 하겠다.

스프링에 객체에 주입하는 방법은 4가지가 존재한다 .

생성자 주입
필드 주입
메서드 주입
수정자 주입
생성자 주입
생성자를 통해 주입을 하는 방식이다.

@Component  
public class MemberServiceImpl implements MemberService{

private final MemberRepository repository;

@Autowired  
public MemberServiceImpl(MemberRepository repository) {  
this.repository = repository;  
}
}
생성자를 통해 주입하는 방식이다. 생성자 위에 있는 @Autowired는 제거 해도 상관없다. class의 생성자가 1개만 존재한다면 자동으로 주입을 해준다. (스프링 빈일때만 그런 것이다. 프레임워크를 다른 것을 사용하는 사람은 참조 바란다.)

필드 주입
@Component  
public class MemberServiceImpl implements
MemberService{

@Autowired   
private final MemberRepository repository;

}
필드에 @Autowired를 통해 객체를 주입해준다. 개인적으로는 필드 주입 방식을 많이 봤던 것 같다.

메서드 주입
@Component  
public class MemberServiceImpl implements
MemberService{

private final MemberRepository repository;

public void init(MemoryMemberRepository memoryMemberRepository)
this.repository = memoryMemberRepository;
}
일단 메서드를 통해 객체를 주입하는 방식.

수정자 주입
@Component  
public class MemberServiceImpl implements
MemberService{

private final MemberRepository repository;

public void setter(MemoryMemberRepository memoryMemberRepository) {
this.repository = memoryMemberRepository;
}
}
setter 수정자를 제공하여 객체를 주입하는 방식이다.

이렇게 4가지의 주입방식을 살펴보았다.
그리고 내가 하고 싶은 말은 “어떤 것을 어떨 때 사용해야 좋을까 ?!” 이다.

개발을 하면서 하나가 무조건 좋다고 말할 수 없다. 적재적소가 필요하다.

하지만 DI의 경우 -> 많은 사람들(필자가 수강했던 강의 강사, DI와 관련된 포스팅, 스프링 공식문서)이 생성자 주입을 많이 사용하고 ,
사용하도록 권고한다.

위 의견에 동의하는 바이다.
테스트와 관련하여 생성자 주입이 꽤 도움이 된다. 우선 스프링 등록된 빈을 이용해 주입을 해줘야 한다면 @SpringBootTest -> 을 통해서 스프링 기동이 필요할 수 있다. 이러면 꽤 오랜 시간을 잡아 먹을 수 있다.

때문에 생성자를 통해 원하는 객체를 직접 초기화하여 테스트할 수 있기 때문에 생성자 주입을 주로 사용할 것이다. 그렇게 습관을 형성하고 있다.

역시 이것도 상황에 적절하지 못하다면 사용하지 않는 것이 좋을 수 있다.
그리고 나의 포스팅은 30%만 신뢰하길 바란다.

나도 나를 의심하면서 글을 작성합니다.

Written with StackEdit.

Markdown 1987 bytes 298 words 89 lines Ln 89, Col 50HTML 1418 characters 289 words 56 paragraphs
WORKSPACES
