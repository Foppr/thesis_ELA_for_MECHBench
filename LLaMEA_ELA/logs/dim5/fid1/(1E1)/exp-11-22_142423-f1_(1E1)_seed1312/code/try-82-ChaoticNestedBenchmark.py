import numpy as np

class ChaoticNestedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with dynamic scaling
        f = np.sum(x**2) * (1.0 + 0.1 * np.sin(3.0 * np.sum(x**2)))
        
        # Add chaotic sinusoidal modulations with varying frequencies
        for i in range(self.dim):
            f += 0.5 * np.sin(7 * x[i]) * np.cos(5 * x[(i + 1) % self.dim]) * np.sin(3 * x[(i + 2) % self.dim])
            
        # Add polynomial coupling with dynamic exponents
        for i in range(self.dim):
            f += 0.3 * (x[i]**4 + x[(i + 1) % self.dim]**3) * np.cos(2 * x[i]) + 0.2 * x[i]**5
            
        # Add nested local minima with varying intensities
        for i in range(self.dim):
            f += 0.4 * np.sin(10 * x[i] + 1.5) * np.cos(6 * x[(i + 1) % self.dim]) * np.sin(4 * x[(i + 2) % self.dim])
            
        # Add dynamic scaling factors based on dimension position
        for i in range(self.dim):
            scale_factor = 1.0 + 0.2 * np.sin(0.5 * i)
            f += 0.15 * scale_factor * x[i]**6
            
        # Add chaotic cross-dimensional interactions with phase shifts
        for i in range(self.dim):
            f += 0.25 * np.cos(8 * x[i]) * np.sin(4 * x[(i + 3) % self.dim]) * np.cos(6 * x[(i + 4) % self.dim]) + 0.1 * np.sin(9 * x[i])
            
        # Add irregular penalty terms with non-uniform exponents
        f += 0.2 * np.sum(np.abs(x)**2.3) + 0.1 * np.sum(x**4)
        
        # Add higher-order chaotic interactions
        for i in range(self.dim):
            f += 0.18 * x[i]**3 * x[(i + 2) % self.dim]**2 * np.sin(5 * x[i]) + 0.12 * x[i]**2 * x[(i + 3) % self.dim]**3 * np.cos(4 * x[(i + 1) % self.dim])
            
        return f