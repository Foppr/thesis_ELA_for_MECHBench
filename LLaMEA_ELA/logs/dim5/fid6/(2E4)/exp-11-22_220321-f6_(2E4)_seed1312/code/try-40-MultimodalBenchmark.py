import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.delay = 3
        self.adaptation_factor = 0.2
        self.fractal_exp = 1.5
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with dynamic scaling
        result = 0.0
        for i in range(self.dim):
            result += (x[i] ** 2) * (1 + self.adaptation_factor * np.sin(i * 1.7))
            
        # Chaotic component using multi-scale delayed feedback
        chaotic_term = 0.0
        for i in range(self.dim):
            delayed_idx1 = (i - self.delay) % self.dim
            delayed_idx2 = (i - 2*self.delay) % self.dim
            if delayed_idx1 < 0:
                delayed_idx1 += self.dim
            if delayed_idx2 < 0:
                delayed_idx2 += self.dim
            chaotic_term += np.sin(x[i] + 0.3 * x[delayed_idx1] + 0.1 * x[delayed_idx2]) * \
                           np.cos(3 * x[i]) * np.exp(-0.05 * x[i]**2)
            
        # Multi-frequency modulation with fractal-like behavior
        freq_mod = 0.0
        for i in range(self.dim):
            freq = (2 ** (i % 5) + 0.5 * np.sin(i)) * (1 + 0.4 * np.cos(x[i]))
            freq_mod += np.sin(freq * x[i]) * np.cos(freq * x[(i + 3) % self.dim]) * \
                       np.exp(-0.1 * np.abs(x[i]))
            
        # Cross-dimensional interaction with nested coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                delayed_i = (i - self.delay) % self.dim
                delayed_j = (j - self.delay) % self.dim
                if delayed_i < 0:
                    delayed_i += self.dim
                if delayed_j < 0:
                    delayed_j += self.dim
                    
                coupling = np.sin(2 * x[i]) * np.cos(2 * x[j]) + \
                          0.2 * np.sin(x[delayed_i]) * np.cos(x[delayed_j])
                cross_term += coupling * np.exp(-0.05 * (x[i] - x[j])**2) * \
                             np.sin(4 * (x[i] + x[j]))
                
        # Fractal-like penalty with nested local minima
        penalty = 0.0
        for i in range(self.dim):
            term = x[i]**(2 * self.fractal_exp) + x[i]**(self.fractal_exp) + \
                   0.5 * np.sin(i) * x[i]**4
            penalty += term * (1 + 0.3 * np.cos(i * 2))
            
        # Add a global perturbation to increase landscape complexity
        global_perturb = 0.0
        for i in range(self.dim):
            global_perturb += np.sin(5 * x[i]) * np.cos(7 * x[(i + 1) % self.dim]) * \
                             np.exp(-0.02 * (x[i]**2 + x[(i + 1) % self.dim]**2))
            
        return result + 0.4 * chaotic_term + 0.3 * freq_mod + 0.2 * cross_term + \
               0.3 * penalty + 0.15 * global_perturb