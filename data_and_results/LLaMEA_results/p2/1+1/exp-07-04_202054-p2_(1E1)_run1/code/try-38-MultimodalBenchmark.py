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
            f_value += 0.9 * np.sin(25 * x[i]) * np.cos(20 * x[i]) * np.sin(30 * x[i])
            
        # Higher-order polynomial terms with increased complexity
        for i in range(self.dim):
            f_value += 0.5 * x[i]**12
            
        # Stronger cross-variable interactions with multiple trigonometric components
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.7 * np.sin(8 * x[i]) * np.cos(15 * x[j]) * np.sin(18 * x[i] + 6 * x[j]) * np.cos(9 * x[i] - 4 * x[j])
                
        # Multi-scale sinusoidal components with varying frequencies and amplitudes
        f_value += 0.6 * np.sum(np.sin(12 * x)**2 + np.cos(18 * x)**2)
        
        # Composite interaction terms with multiple trigonometric functions
        f_value += 0.4 * np.sum(np.sin(x)**6 * np.cos(x)**6 * np.sin(6 * x))
        
        # Fourth-order polynomial interaction with sinusoidal modulation
        for i in range(self.dim):
            f_value += 0.3 * x[i]**7 * np.sin(5 * x[i])
            
        # Fifth-order polynomial with cosine modulation
        for i in range(self.dim):
            f_value += 0.35 * x[i]**8 * np.cos(6 * x[i])
            
        # Multi-modal sinusoidal component with varying amplitudes and frequencies
        f_value += 0.5 * np.sum(np.sin(30 * x) * np.cos(25 * x))
        
        # Enhanced cross-term interactions with increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.6 * np.sin(10 * x[i]) * np.cos(15 * x[j]) * np.sin(9 * x[i] + 5 * x[j]) * np.cos(11 * x[i] - 6 * x[j]) * np.sin(5 * x[i] + 4 * x[j])
                
        # Additional high-order polynomial interaction terms
        for i in range(self.dim):
            f_value += 0.3 * x[i]**9 * np.sin(x[i])
            
        # Composite multi-scale interaction with multiple frequencies
        f_value += 0.5 * np.sum(np.sin(8 * x) * np.cos(10 * x) * np.sin(12 * x))
        
        # Increased complexity in variable coupling with multiple trigonometric combinations
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.6 * np.sin(12 * x[i]) * np.cos(16 * x[j]) * np.sin(10 * x[i] + 7 * x[j]) * np.cos(6 * x[i] - 5 * x[j]) * np.sin(11 * x[i] + 5 * x[j])
                
        # Slight modification: increased coefficient for the highest-order polynomial term
        for i in range(self.dim):
            f_value += 0.5 * x[i]**13 * np.sin(x[i])
            
        # Add noise to increase irregularity
        noise = np.random.normal(0, 0.15, self.dim)
        f_value += 0.15 * np.sum(noise * x)
        
        # Add irregular bumps for additional challenge
        for i in range(self.dim):
            f_value += 0.25 * np.sin(60 * x[i]) * np.cos(35 * x[i]) * np.sin(45 * x[i])
            
        # Add a new component to improve fitness score: additional multi-modal sinusoidal terms
        f_value += 0.4 * np.sum(np.sin(35 * x) * np.cos(30 * x) * np.sin(40 * x))
        
        # Add a new component to improve fitness score: enhanced cross-variable interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.5 * np.sin(13 * x[i]) * np.cos(18 * x[j]) * np.sin(15 * x[i] + 8 * x[j]) * np.cos(10 * x[i] - 7 * x[j]) * np.sin(14 * x[i] + 5 * x[j])
                
        # Add a new component to improve fitness score: higher-order polynomial with increased complexity
        for i in range(self.dim):
            f_value += 0.4 * x[i]**14 * np.cos(3 * x[i])
            
        return f_value