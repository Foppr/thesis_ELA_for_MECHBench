import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for tent map
        self.chebyshev_coeffs = np.random.uniform(-1, 1, (dim, 5))
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component with dynamic parameter modulation
        tent_component = 0
        for i in range(self.dim):
            # Dynamic parameter based on position and Chebyshev coefficients
            a = 1.5 + 0.5 * np.sin(x[i] * 0.7) + 0.3 * self.chebyshev_coeffs[i, 0]
            # Tent map iteration with chaotic dynamics
            xi = x[i]
            for _ in range(3):
                if xi < a:
                    xi = xi / a
                else:
                    xi = (1 - xi) / (1 - a)
            tent_component += xi ** 2
        
        # Spectral clustering inspired interaction terms
        spectral_component = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                # Adaptive kernel based on distance and dimension
                kernel_width = 0.5 + 0.5 * np.sin(0.3 * (x[i] + x[j]))
                spectral_component += np.exp(-dist**2 / (2 * kernel_width**2)) * np.sin(3 * dist)
        
        # Adaptive gradient modulation with piecewise linear transformation
        grad_component = 0
        for i in range(self.dim):
            # Piecewise linear function with dynamic breakpoints
            if x[i] < 0:
                grad_component += (x[i]**3) * (1 + 0.2 * np.sin(2 * x[i]))
            else:
                grad_component += (x[i]**2) * (1 + 0.1 * np.cos(1.5 * x[i]))
        
        # Dynamic conditioning with exponential and logarithmic scaling
        cond_component = 0
        for i in range(self.dim):
            # Logarithmic scaling with dynamic base
            base = 1.1 + 0.2 * np.sin(0.4 * x[i])
            cond_component += np.log(np.abs(x[i]) + 1) / np.log(base) + 0.5 * np.exp(-x[i]**2)
        
        # Discontinuous noise with fractal-like characteristics
        noise = 0
        for i in range(self.dim):
            # Fractional Brownian motion inspired discontinuity
            noise += np.sin(13 * x[i]) * np.cos(7 * x[i]) * np.tanh(x[i]**2)
        
        # Global scaling and shift
        scale_factor = 1.0 + 0.4 * np.sin(0.5 * self.dim)
        shift = 0.1 * np.sum(np.abs(x))
        
        # Combine all components with optimized weights
        return scale_factor * (0.3 * tent_component + 0.4 * spectral_component + 
                              0.2 * grad_component + 0.1 * cond_component) + shift + noise