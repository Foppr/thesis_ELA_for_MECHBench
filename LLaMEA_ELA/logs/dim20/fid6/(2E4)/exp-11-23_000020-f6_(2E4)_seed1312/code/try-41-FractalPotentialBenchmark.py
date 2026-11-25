import numpy as np

class FractalPotentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal dimensions and scaling factors
        self.fractal_dims = 1.0 + np.random.rand(dim) * 2.0  # Fractional dimensions
        self.scales = np.logspace(-1, 1, dim)  # Scale factors for multi-scale effects
        self.poly_orders = np.random.randint(3, 7, dim)  # Polynomial orders
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Fractal geometric component using self-similar patterns
        fractal = 0.0
        for i in range(self.dim):
            # Create fractal-like behavior using recursive-like scaling
            scale = self.scales[i]
            dim_factor = self.fractal_dims[i]
            # Simulate fractal pattern with multi-scale sine waves
            fractal += np.sin(scale * x_norm[i] ** dim_factor) * np.cos(scale * x_norm[i] ** (dim_factor / 2))
        
        # Adaptive polynomial potentials with dynamic exponents
        poly_potential = 0.0
        for i in range(self.dim):
            order = self.poly_orders[i]
            # Use adaptive polynomial terms with varying coefficients
            coeff = np.sin(i) * 0.5 + 0.75
            poly_potential += coeff * (x_norm[i] ** order)
            
        # Dynamic gradient field component with directional coupling
        gradient_field = 0.0
        for i in range(self.dim):
            # Create directionally dependent gradient terms
            grad_term = np.cos(x_norm[i]) * np.sin(x_norm[(i + 1) % self.dim])
            # Add varying strength based on dimension index
            strength = 1.0 / (1.0 + np.exp(-i))
            gradient_field += strength * grad_term
            
        # Multi-scale harmonic interference pattern
        harmonic = 0.0
        for i in range(self.dim):
            freq = 2 ** (i % 4)  # Varying frequencies
            # Combine multiple harmonics with different phases
            harmonic += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] / 2.0)
            
        # Cross-dimensional coupling with exponential decay
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                # Exponentially decaying interaction between dimensions
                decay = np.exp(-0.5 * (x_norm[i] - x_norm[j])**2)
                coupling += decay * np.sin(x_norm[i] + x_norm[j])
                
        # Global scaling and modulation using golden ratio
        phi = (1 + np.sqrt(5)) / 2
        modulator = np.sum(np.sin(phi * x_norm) + np.cos(phi * x_norm))
        
        # Combine all components with dynamic weights
        result = (0.25 * fractal + 
                 0.30 * poly_potential + 
                 0.20 * gradient_field + 
                 0.15 * harmonic + 
                 0.10 * coupling + 
                 0.05 * modulator)
        
        # Add a global rotation and shift to increase problem difficulty
        return result + 0.5 * np.sin(np.sum(x_norm**2) / self.dim) * np.cos(np.sum(x_norm))