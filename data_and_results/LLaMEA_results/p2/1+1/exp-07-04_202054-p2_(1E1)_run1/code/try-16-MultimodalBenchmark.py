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
            f_value += 0.6 * np.sin(12 * x[i]) * np.cos(10 * x[i]) * np.sin(14 * x[i])
            
        # Higher-order polynomial terms with increased complexity
        for i in range(self.dim):
            f_value += 0.25 * x[i]**7
            
        # Stronger cross-variable interactions with multiple trigonometric components
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.35 * np.sin(4 * x[i]) * np.cos(6 * x[j]) * np.sin(8 * x[i] + 4 * x[j]) * np.cos(5 * x[i] - 2 * x[j])
                
        # Multi-scale sinusoidal components with varying frequencies and amplitudes
        f_value += 0.3 * np.sum(np.sin(7 * x)**2 + np.cos(10 * x)**2)
        
        # Composite interaction terms with multiple trigonometric functions
        f_value += 0.2 * np.sum(np.sin(x)**3 * np.cos(x)**3 * np.sin(4 * x))
        
        # Fourth-order polynomial interaction with sinusoidal modulation
        for i in range(self.dim):
            f_value += 0.15 * x[i]**4 * np.sin(3 * x[i])
            
        # Fifth-order polynomial with cosine modulation
        for i in range(self.dim):
            f_value += 0.2 * x[i]**5 * np.cos(4 * x[i])
            
        # Multi-modal sinusoidal component with varying amplitudes and frequencies
        f_value += 0.25 * np.sum(np.sin(16 * x) * np.cos(12 * x))
        
        # Enhanced cross-term interactions with increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.3 * np.sin(6 * x[i]) * np.cos(8 * x[j]) * np.sin(5 * x[i] + 3 * x[j]) * np.cos(7 * x[i] - 4 * x[j]) * np.sin(3 * x[i] + 2 * x[j])
                
        # Additional high-order polynomial interaction terms
        for i in range(self.dim):
            f_value += 0.15 * x[i]**6 * np.sin(x[i])
            
        # Composite multi-scale interaction with multiple frequencies
        f_value += 0.22 * np.sum(np.sin(5 * x) * np.cos(7 * x) * np.sin(9 * x))
        
        # Increased complexity in variable coupling with multiple trigonometric combinations
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.35 * np.sin(7 * x[i]) * np.cos(10 * x[j]) * np.sin(6 * x[i] + 5 * x[j]) * np.cos(4 * x[i] - 3 * x[j]) * np.sin(8 * x[i] + 2 * x[j])
                
        # Slight modification: increased coefficient for the highest-order polynomial term
        for i in range(self.dim):
            f_value += 0.3 * x[i]**8 * np.sin(x[i])
            
        return f_value