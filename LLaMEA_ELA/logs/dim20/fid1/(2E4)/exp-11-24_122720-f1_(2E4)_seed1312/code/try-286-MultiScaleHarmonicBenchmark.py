import numpy as np

class MultiScaleHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize harmonic parameters for each dimension
        self.frequencies = [np.random.uniform(1.0, 5.0) for _ in range(dim)]
        self.amplitudes = [np.random.uniform(0.5, 2.0) for _ in range(dim)]
        self.damping_factors = [np.random.uniform(0.1, 0.5) for _ in range(dim)]
        self.scale_factors = [np.random.uniform(0.5, 2.0) for _ in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Multi-scale harmonic component
        harmonic = 0
        for i in range(self.dim):
            freq = self.frequencies[i]
            amp = self.amplitudes[i]
            scale = self.scale_factors[i]
            # Scale and apply harmonic function with damping
            scaled_x = x[i] * scale
            harmonic += amp * np.sin(freq * scaled_x) * np.exp(-self.damping_factors[i] * np.abs(x[i]))
            
        # Nested periodic structure with varying periods
        nested = 0
        for i in range(self.dim):
            # Create nested oscillations with increasing frequency
            period = 2 * np.pi / (i + 1)
            nested += np.cos(period * x[i]) * np.sin(3 * period * x[i])
            
        # Gradient-dependent damping component
        gradient_damping = 0
        for i in range(self.dim):
            grad_term = np.cos(x[i]) * np.sin(x[i])
            damping = self.damping_factors[i] * (1 + 0.5 * np.abs(grad_term))
            gradient_damping += damping * np.exp(-0.1 * x[i]**2)
            
        # Cross-dimension coupling with scale modulation
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Scale-modulated coupling term
                coupling_factor = self.scale_factors[i] * self.scale_factors[j]
                coupling += coupling_factor * np.sin(x[i]) * np.cos(x[j])
                
        # Combine components with dynamic weights
        result = 0.7 * harmonic + 0.5 * nested + 0.3 * gradient_damping + 0.2 * coupling
        
        # Add dimensionality scaling effect
        dim_scaling = 1.0 + 0.1 * np.log(self.dim + 1)
        result *= dim_scaling
        
        return result