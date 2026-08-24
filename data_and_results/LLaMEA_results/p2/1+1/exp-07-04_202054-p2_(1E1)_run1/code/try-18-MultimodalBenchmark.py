import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global minimum
        f_value = np.sum(x**2)
        
        # High-frequency trigonometric perturbations with increased amplitude
        for i in range(self.dim):
            f_value += 0.5 * np.sin(10 * x[i]) * np.cos(8 * x[i]) * np.sin(12 * x[i])
            
        # Higher-order polynomial terms with increased complexity
        for i in range(self.dim):
            f_value += 0.2 * x[i]**7
            
        # Stronger cross-variable interactions with multiple trigonometric components
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.3 * np.sin(3 * x[i]) * np.cos(5 * x[j]) * np.sin(7 * x[i] + 3 * x[j]) * np.cos(4 * x[i] - x[j])
                
        # Multi-scale sinusoidal components with varying frequencies and amplitudes
        f_value += 0.25 * np.sum(np.sin(6 * x)**2 + np.cos(9 * x)**2)
        
        # Composite interaction terms with multiple trigonometric functions
        f_value += 0.15 * np.sum(np.sin(x)**3 * np.cos(x)**3 * np.sin(3 * x))
        
        # Fourth-order polynomial interaction with sinusoidal modulation
        for i in range(self.dim):
            f_value += 0.12 * x[i]**4 * np.sin(2 * x[i])
            
        # Fifth-order polynomial with cosine modulation
        for i in range(self.dim):
            f_value += 0.18 * x[i]**5 * np.cos(3 * x[i])
            
        # Multi-modal sinusoidal component with varying amplitudes and frequencies
        f_value += 0.2 * np.sum(np.sin(15 * x) * np.cos(11 * x))
        
        # Enhanced cross-term interactions with increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.25 * np.sin(5 * x[i]) * np.cos(7 * x[j]) * np.sin(4 * x[i] + 2 * x[j]) * np.cos(6 * x[i] - 3 * x[j]) * np.sin(2 * x[i] + x[j])
                
        # Additional high-order polynomial interaction terms
        for i in range(self.dim):
            f_value += 0.1 * x[i]**6 * np.sin(x[i])
            
        # Composite multi-scale interaction with multiple frequencies
        f_value += 0.18 * np.sum(np.sin(4 * x) * np.cos(6 * x) * np.sin(8 * x))
        
        # Increased complexity in variable coupling with multiple trigonometric combinations
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.3 * np.sin(6 * x[i]) * np.cos(9 * x[j]) * np.sin(5 * x[i] + 4 * x[j]) * np.cos(3 * x[i] - 2 * x[j]) * np.sin(7 * x[i] + x[j])
                
        # Slight modification: increased coefficient for the highest-order polynomial term
        for i in range(self.dim):
            f_value += 0.25 * x[i]**8 * np.sin(x[i])
            
        # Add a small perturbation to increase difficulty
        f_value += 0.05 * np.sum(np.sin(20 * x) * np.cos(18 * x))
        
        return f_value