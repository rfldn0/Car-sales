Here's a formatted version of your project description for a `README.md` file:

```markdown
# CS/CYCS1120 (Python) – Fall 2022  
## Programming Project #4  

**Due Date** (Two-week Project)  
**200 points**  
**Tuesday Labs – 10/25/22 @ 11:59pm**  

---

### Project Objectives  
- Reviewing OOP  
- Reviewing Inheritance  
- Reviewing File I/O  

---

### Project Overview  
A store has classified the types of cars it is selling as either **imported cars** or **domestic cars**.  

Your program should have:  
- **One superclass** called `Car`  
- **Two derived classes**: `ImportCar` and `DomesticCar`  

#### **Superclass `Car`**  
Keeps common information:  
- Brand  
- Model  
- Year  
- Type  
- Price  

#### **Subclasses**  
1. **`ImportCar`** (extends `Car`)  
   - Additional attributes:  
     - `Country` (export country)  
     - `Tax` (import tax %)  
2. **`DomesticCar`** (extends `Car`)  
   - Additional attribute:  
     - `State` (where the car was produced)  
   - *No additional tax is levied on domestic cars.*  

#### **Access Control & Methods**  
- All data fields must be **private** (`__attribute`).  
- Use **accessor methods** (`get`/`set`) to interact with private members.  
- The superclass `__init__()` method should be called during subclass initialization.  

---

### Class Structure  

#### **`Car` (Superclass)**  
```python
__Brand  
__Model  
__Year  
__Price  
__Type  

get_brand()  
set_brand()  
get_model()  
set_model()  
get_year()  
set_year()  
get_price()  
set_price()  
get_type()  
set_type()  
print_info()  
```

#### **`ImportCar` (Subclass)**  
```python
__Country  
__Tax  

get_country()  
set_country()  
get_tax()  
set_tax()  
print_info()  # Overrides superclass method  
```

#### **`DomesticCar` (Subclass)**  
```python
__State  

get_state()  
set_state()  
print_info()  # Overrides superclass method  
```

---

### Implementation Notes  
- Ensure proper **inheritance** (`super()` usage).  
- Follow **encapsulation** (private attributes + getters/setters).  
- Include **file I/O** for data persistence if required.  
```

This version is properly formatted for GitHub's Markdown rendering and includes clear section headings, code blocks, and bullet points for readability. You can copy this directly into your `README.md` file.
