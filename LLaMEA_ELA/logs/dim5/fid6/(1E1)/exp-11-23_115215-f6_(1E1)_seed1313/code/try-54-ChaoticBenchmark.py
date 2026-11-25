import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute tent map parameters for enhanced chaos
        self.a_values = np.linspace(1.5, 1.9, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add chaotic tent map components
        for i in range(self.dim):
            # Tent map with parameter a_i
            if i == 0:
                tent_val = x[i]
            else:
                tent_val = self.a_values[i] * min(x[i-1], 1 - x[i-1])
            f_val += 0.4 * np.sin(tent_val * 15) * np.cos(tent_val * 11)
            
        # Add quantum-inspired radial basis function components with complex widths
        for i in range(self.dim):
            # Quantum-like RBF with dynamic center and complex width
            center = np.sin(i * 0.7) * 4.0
            width = 0.3 + 0.7 * np.abs(np.cos(i * 0.4)) * np.sin(i * 0.2)
            f_val += 0.3 * np.exp(-0.5 * ((x[i] - center) / width)**3) * np.sin(x[i])
            
        # Add fractal coupling terms with self-similar patterns
        for i in range(self.dim):
            if i > 0:
                # Fractal interaction: scaling factor based on dimension index
                scale = 0.1 * (i + 1)**(-1.2)
                f_val += scale * (x[i] - x[i-1])**4 + 0.05 * np.abs(x[i] - x[i-1])**2.3
                
        # Add multi-scale fractal sinusoidal modulations
        for i in range(self.dim):
            f_val += 0.3 * np.sin(3 * x[i]) * np.cos(5 * x[i]) + \
                     0.15 * np.sin(7 * x[i]) * np.cos(9 * x[i]) + \
                     0.08 * np.sin(13 * x[i]) * np.cos(17 * x[i]) + \
                     0.03 * np.sin(23 * x[i])
                     
        # Add polynomial coupling with fractal weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal weight based on dimension indices
                weight = (i + j + 1)**(-1.5) * np.sin(i * j * 0.1)
                f_val += weight * (x[i]**3) * (x[j]**2) + 0.07 * x[i] * x[j]
                
        # Add fractal phase coupling with multi-delayed terms
        for i in range(self.dim):
            if i > 2:
                delayed_term = np.sin(x[i-3] + 0.3 * x[i-2] + 0.7 * x[i-1])
                f_val += 0.15 * delayed_term * np.cos(x[i] * 0.5)
                
        # Add a final fractal non-linear transformation
        f_val += 0.15 * np.sin(np.sum(x**4)) + 0.08 * np.cos(np.prod(x)) + \
                 0.05 * np.sin(np.sum(np.abs(x)**2.5))
        
        return f_val