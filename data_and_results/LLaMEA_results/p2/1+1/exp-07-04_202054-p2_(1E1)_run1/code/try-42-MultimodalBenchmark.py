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
            f_value += 0.8 * np.sin(20 * x[i]) * np.cos(15 * x[i]) * np.sin(25 * x[i])
            
        # Higher-order polynomial terms with increased complexity
        for i in range(self.dim):
            f_value += 0.4 * x[i]**11
            
        # Stronger cross-variable interactions with multiple trigonometric components
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.6 * np.sin(7 * x[i]) * np.cos(12 * x[j]) * np.sin(15 * x[i] + 5 * x[j]) * np.cos(8 * x[i] - 3 * x[j])
                
        # Multi-scale sinusoidal components with varying frequencies and amplitudes
        f_value += 0.5 * np.sum(np.sin(10 * x)**2 + np.cos(15 * x)**2)
        
        # Composite interaction terms with multiple trigonometric functions
        f_value += 0.3 * np.sum(np.sin(x)**5 * np.cos(x)**5 * np.sin(5 * x))
        
        # Fourth-order polynomial interaction with sinusoidal modulation
        for i in range(self.dim):
            f_value += 0.25 * x[i]**6 * np.sin(4 * x[i])
            
        # Fifth-order polynomial with cosine modulation
        for i in range(self.dim):
            f_value += 0.3 * x[i]**7 * np.cos(5 * x[i])
            
        # Multi-modal sinusoidal component with varying amplitudes and frequencies
        f_value += 0.4 * np.sum(np.sin(25 * x) * np.cos(20 * x))
        
        # Enhanced cross-term interactions with increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.5 * np.sin(9 * x[i]) * np.cos(13 * x[j]) * np.sin(8 * x[i] + 4 * x[j]) * np.cos(10 * x[i] - 5 * x[j]) * np.sin(4 * x[i] + 3 * x[j])
                
        # Additional high-order polynomial interaction terms
        for i in range(self.dim):
            f_value += 0.25 * x[i]**8 * np.sin(x[i])
            
        # Composite multi-scale interaction with multiple frequencies
        f_value += 0.4 * np.sum(np.sin(7 * x) * np.cos(9 * x) * np.sin(11 * x))
        
        # Increased complexity in variable coupling with multiple trigonometric combinations
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.5 * np.sin(10 * x[i]) * np.cos(14 * x[j]) * np.sin(9 * x[i] + 6 * x[j]) * np.cos(5 * x[i] - 4 * x[j]) * np.sin(10 * x[i] + 3 * x[j])
                
        # Slight modification: increased coefficient for the highest-order polynomial term
        for i in range(self.dim):
            f_value += 0.4 * x[i]**12 * np.sin(x[i])
            
        # Add noise to increase irregularity
        noise = np.random.normal(0, 0.1, self.dim)
        f_value += 0.1 * np.sum(noise * x)
        
        # Add irregular bumps for additional challenge
        for i in range(self.dim):
            f_value += 0.2 * np.sin(50 * x[i]) * np.cos(30 * x[i]) * np.sin(40 * x[i])
            
        # Add a new component to improve fitness score: additional multi-modal sinusoidal terms
        f_value += 0.3 * np.sum(np.sin(30 * x) * np.cos(25 * x) * np.sin(35 * x))
        
        # Add a new component to improve fitness score: enhanced cross-variable interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.4 * np.sin(11 * x[i]) * np.cos(16 * x[j]) * np.sin(13 * x[i] + 7 * x[j]) * np.cos(9 * x[i] - 6 * x[j]) * np.sin(12 * x[i] + 4 * x[j])
                
        # Add a new component to improve fitness score: higher-order polynomial with increased complexity
        for i in range(self.dim):
            f_value += 0.35 * x[i]**13 * np.cos(2 * x[i])
            
        # Additional modification: introduce a new high-frequency sinusoidal term with a different amplitude and frequency
        f_value += 0.2 * np.sum(np.sin(60 * x) * np.cos(45 * x))
        
        # Additional modification: increase the complexity of one of the interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.3 * np.sin(14 * x[i]) * np.cos(18 * x[j]) * np.sin(16 * x[i] + 9 * x[j]) * np.cos(11 * x[i] - 7 * x[j]) * np.sin(13 * x[i] + 6 * x[j])
                
        return f_value