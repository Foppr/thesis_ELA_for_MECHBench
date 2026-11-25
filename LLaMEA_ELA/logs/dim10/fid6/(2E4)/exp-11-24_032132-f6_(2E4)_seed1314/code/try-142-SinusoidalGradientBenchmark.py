import numpy as np

class SinusoidalGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.num_waves = 6
        self.adaptation_rate = 0.1
        self.saddle_density = 0.3
        self.gradient_magnitude = 2.0
        
    def f(self, x):
        # Handle dimension mismatch
        if len(x) < self.dim:
            raise ValueError("Dimension mismatch: input has fewer dimensions than expected")
        elif len(x) > self.dim:
            x = x[:self.dim]
        
        # Scale input to [-5, 5] range if needed
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        result = 0.0
        
        # Sinusoidal wave component with varying frequencies and amplitudes
        for i in range(self.num_waves):
            freq = 1.0 + i * 0.5
            amp = 1.0 + i * 0.3
            phase = i * np.pi / 4
            
            # Multi-dimensional sinusoidal term
            wave_term = amp * np.sin(freq * np.sum(x) + phase)
            result += wave_term
        
        # Adaptive gradient field component
        grad_field = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Gradient magnitude modulated by position and adaptation rate
            grad_magnitude = self.gradient_magnitude * (1.0 + 0.5 * np.sin(xi * 0.8))
            grad_field += grad_magnitude * xi
            
        # Saddle-point structure with density control
        saddle_term = 0.0
        for i in range(self.dim):
            if np.random.rand() < self.saddle_density:
                # Add saddle point contribution
                saddle_term += (x[i] ** 2 - 1.0) ** 2
        
        # Combine components with dynamic weighting
        total_components = 3.0 + np.sin(np.sum(x) * 0.5)
        return (0.4 * result + 0.3 * grad_field + 0.3 * saddle_term) / total_components