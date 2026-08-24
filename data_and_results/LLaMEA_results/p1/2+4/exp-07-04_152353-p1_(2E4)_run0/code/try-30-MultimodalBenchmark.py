import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Quadratic base with varying weights
        f1 = np.sum(x_normalized**2)
        
        # High-frequency sinusoidal components with phase shifts
        f2 = np.sum(np.sin(7 * np.pi * x_normalized) * np.cos(5 * np.pi * x_normalized))
        
        # Exponential decay with sinusoidal modulation
        f3 = np.sum(np.exp(-3 * x_normalized**2) * np.sin(6 * np.pi * x_normalized))
        
        # Complex interaction terms with asymmetric coupling and higher-order polynomials
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Asymmetric interaction with cubic and quadratic terms
                interaction += (x_normalized[i]**4 - x_normalized[j]**3)**2 + 0.5 * (x_normalized[i]**2 - x_normalized[j])**4
        
        # Global minimum with polynomial and periodic components
        result = 0.25 * f1 + 0.3 * f2 + 0.2 * f3 + 0.25 * interaction
        
        # Stronger periodic modulation to increase local minima density
        periodic_mod = np.sum(np.sin(3 * np.pi * x_normalized) * np.cos(3 * np.pi * x_normalized) + 
                             0.3 * np.sin(9 * np.pi * x_normalized))
        result += 0.1 * periodic_mod
        
        # Enhanced saddle point structure with quartic and sextic terms
        saddle = np.sum(x_normalized**6 - 3 * x_normalized**4 + 2 * x_normalized**2)
        result += 0.05 * saddle
        
        # Add a small noise component to increase problem difficulty
        noise = 0.01 * np.sum(np.sin(10 * np.pi * x_normalized) * np.cos(8 * np.pi * x_normalized))
        result += noise
        
        # Add higher-order polynomial interactions for increased complexity
        high_order = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    high_order += (x_normalized[i]**5 * x_normalized[j]**3 + x_normalized[k]**4) ** 2
        
        result += 0.03 * high_order
        
        # Add a more complex periodic modulation with multiple frequencies
        complex_periodic = np.sum(np.sin(4 * np.pi * x_normalized) * np.cos(7 * np.pi * x_normalized) + 
                                np.sin(2 * np.pi * x_normalized) * np.cos(9 * np.pi * x_normalized) + 
                                0.5 * np.sin(11 * np.pi * x_normalized))
        result += 0.08 * complex_periodic
        
        # Add asymmetric coupling terms with exponential decay
        asymmetric = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                asymmetric += np.exp(-2 * (x_normalized[i] - x_normalized[j])**2) * (x_normalized[i]**3 - x_normalized[j]**2)**2
        
        result += 0.04 * asymmetric
        
        # Add a global scaling factor to increase the function's overall complexity
        result *= (1 + 0.1 * np.sum(np.sin(13 * np.pi * x_normalized)))
        
        return result