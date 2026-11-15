import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global minimum
        f_value = np.sum(x**2)
        
        # High-frequency trigonometric perturbations with increased amplitude and chaos
        for i in range(self.dim):
            f_value += 1.2 * np.sin(30 * x[i]) * np.cos(25 * x[i]) * np.sin(35 * x[i]) * np.cos(20 * x[i])
            
        # Higher-order polynomial terms with increased complexity and chaotic exponents
        for i in range(self.dim):
            f_value += 0.6 * x[i]**13
            
        # Stronger cross-variable interactions with multiple trigonometric components and chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.8 * np.sin(10 * x[i]) * np.cos(18 * x[j]) * np.sin(15 * x[i] + 8 * x[j]) * np.cos(12 * x[i] - 6 * x[j]) * np.sin(9 * x[i] + 5 * x[j]) * np.cos(14 * x[i] - 7 * x[j])
                
        # Multi-scale sinusoidal components with varying frequencies, amplitudes, and chaotic modulation
        f_value += 0.7 * np.sum(np.sin(15 * x)**3 + np.cos(20 * x)**3 + np.sin(25 * x)**2)
        
        # Composite interaction terms with multiple trigonometric functions and chaotic combinations
        f_value += 0.5 * np.sum(np.sin(x)**7 * np.cos(x)**7 * np.sin(8 * x) * np.cos(6 * x))
        
        # Fourth-order polynomial interaction with sinusoidal modulation and chaotic frequency
        for i in range(self.dim):
            f_value += 0.4 * x[i]**8 * np.sin(6 * x[i]) * np.cos(4 * x[i])
            
        # Fifth-order polynomial with cosine modulation and chaotic component
        for i in range(self.dim):
            f_value += 0.5 * x[i]**9 * np.cos(7 * x[i]) * np.sin(5 * x[i])
            
        # Multi-modal sinusoidal component with varying amplitudes, frequencies, and chaotic patterns
        f_value += 0.6 * np.sum(np.sin(35 * x) * np.cos(30 * x) * np.sin(40 * x) * np.cos(25 * x))
        
        # Enhanced cross-term interactions with increased complexity and chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.7 * np.sin(12 * x[i]) * np.cos(16 * x[j]) * np.sin(14 * x[i] + 9 * x[j]) * np.cos(11 * x[i] - 8 * x[j]) * np.sin(13 * x[i] + 6 * x[j]) * np.cos(15 * x[i] - 5 * x[j])
                
        # Additional high-order polynomial interaction terms with chaotic modulations
        for i in range(self.dim):
            f_value += 0.5 * x[i]**10 * np.sin(5 * x[i]) * np.cos(3 * x[i])
            
        # Composite multi-scale interaction with multiple frequencies and chaotic combinations
        f_value += 0.6 * np.sum(np.sin(12 * x) * np.cos(18 * x) * np.sin(22 * x) * np.cos(15 * x))
        
        # Increased complexity in variable coupling with multiple chaotic trigonometric combinations
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.6 * np.sin(15 * x[i]) * np.cos(20 * x[j]) * np.sin(18 * x[i] + 12 * x[j]) * np.cos(13 * x[i] - 9 * x[j]) * np.sin(16 * x[i] + 10 * x[j]) * np.cos(17 * x[i] - 8 * x[j])
                
        # Slight modification: increased coefficient for the highest-order polynomial term with chaotic modulation
        for i in range(self.dim):
            f_value += 0.6 * x[i]**15 * np.sin(5 * x[i]) * np.cos(4 * x[i])
            
        # Add noise to increase irregularity with chaotic pattern
        noise = np.random.normal(0, 0.15, self.dim)
        f_value += 0.15 * np.sum(noise * x * np.sin(50 * x))
        
        # Add irregular bumps for additional challenge with chaotic frequency
        for i in range(self.dim):
            f_value += 0.3 * np.sin(60 * x[i]) * np.cos(40 * x[i]) * np.sin(50 * x[i]) * np.cos(30 * x[i])
            
        # Add a new component to improve fitness score: additional multi-modal sinusoidal terms with chaotic patterns
        f_value += 0.4 * np.sum(np.sin(40 * x) * np.cos(35 * x) * np.sin(45 * x) * np.cos(30 * x))
        
        # Add a new component to improve fitness score: enhanced cross-variable interactions with chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.5 * np.sin(13 * x[i]) * np.cos(22 * x[j]) * np.sin(16 * x[i] + 11 * x[j]) * np.cos(14 * x[i] - 10 * x[j]) * np.sin(15 * x[i] + 9 * x[j]) * np.cos(17 * x[i] - 12 * x[j])
                
        # Add a new component to improve fitness score: higher-order polynomial with increased complexity and chaotic modulation
        for i in range(self.dim):
            f_value += 0.5 * x[i]**16 * np.cos(3 * x[i]) * np.sin(2 * x[i])
            
        # Slight modification: reduce the influence of the highest-order polynomial term and change modulation to chaotic
        for i in range(self.dim):
            f_value += 0.3 * x[i]**17 * np.sin(4 * x[i]) * np.cos(3 * x[i])
            
        # Add a new component: increased complexity in cross-variable interactions with chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.4 * np.sin(18 * x[i]) * np.cos(25 * x[j]) * np.sin(20 * x[i] + 15 * x[j]) * np.cos(16 * x[i] - 13 * x[j]) * np.sin(19 * x[i] + 14 * x[j]) * np.cos(21 * x[i] - 17 * x[j])
                
        # Add a new component: modified sinusoidal modulation with chaotic pattern
        f_value += 0.35 * np.sum(np.sin(45 * x)**4 + np.cos(35 * x)**4 + np.sin(50 * x)**3)
        
        # Slight modification: reduced coefficient for the highest-order polynomial term and changed modulation to chaotic
        for i in range(self.dim):
            f_value += 0.25 * x[i]**17 * np.cos(5 * x[i]) * np.sin(4 * x[i])
            
        return f_value