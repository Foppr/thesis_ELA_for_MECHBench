import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_depth = min(5, dim)
        self.memory_size = 3
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = 0.1 * np.sum(x**2)
        
        # Fractal recursive structure with nested sinusoidal components
        for i in range(self.fractal_depth):
            scale = 2 ** (self.fractal_depth - i)
            freq = 2 ** i
            f_val += 2.5 * np.sin(freq * x[i % self.dim]) * np.cos(freq * x[i % self.dim] / scale)
            
        # Memory-dependent gradient field using previous evaluations
        memory_term = 0.0
        if hasattr(self, 'history'):
            for i in range(min(self.memory_size, len(self.history))):
                memory_term += 1.2 * np.sin(x[i % self.dim] + self.history[-(i+1)])
        else:
            self.history = []
        self.history.append(np.sum(x))
        
        # Complex frequency modulation with chaotic component
        mod_freq = 1.0
        for i in range(self.dim):
            mod_freq = 3.8 * mod_freq * (1 - mod_freq)
            f_val += 1.8 * np.sin(mod_freq * x[i % self.dim] + 2.5) * np.cos(1.5 * x[i % self.dim])
            
        # Non-smooth fractal peaks with varying heights and widths
        for i in range(self.dim):
            height = 3.0 + 0.5 * np.sin(i)
            width = 0.8 + 0.2 * np.cos(i)
            peak_pos = -4.0 + 2.0 * np.sin(i)
            f_val += height * np.exp(-0.5 * ((x[i % self.dim] - peak_pos) / width)**4)
            
        # Cross-dimensional coupling with recursive interaction
        for i in range(self.dim):
            j = (i + 1) % self.dim
            f_val += 1.3 * x[i % self.dim] * np.sin(x[j]) * np.cos(0.7 * x[i % self.dim])
            
        # Asymmetric saddle points with dynamic scaling
        for i in range(self.dim):
            asym_factor = 1.0 + 0.5 * np.sin(i)
            f_val += asym_factor * (np.exp(-0.5 * (x[i % self.dim] - 1.0)**2) * 
                                   np.sin(0.3 * x[i % self.dim]) + 
                                   np.exp(-0.5 * (x[i % self.dim] + 1.0)**2) * 
                                   np.cos(0.7 * x[i % self.dim]))
            
        # Additive chaotic noise with time-varying amplitude
        chaos_noise = 0.0
        for i in range(self.dim):
            chaos_noise += 0.5 * np.sin(3.14159 * x[i % self.dim] + 0.1 * i)
        f_val += chaos_noise
        
        # Higher-order polynomial terms for increased complexity
        for i in range(self.dim):
            f_val += 0.2 * x[i % self.dim]**6 + 0.1 * x[i % self.dim]**5
            
        return f_val