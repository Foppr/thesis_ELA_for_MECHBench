import numpy as np

class FractalGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_dim = 2.5  # Fractional dimension for fractal behavior
        self.adaptation_rate = 0.3
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal component using box-counting like behavior
        fractal = 0.0
        for i in range(self.dim):
            xi = x[i] / 5.0  # Normalize to [-1, 1]
            # Multi-scale fractal-like contribution
            scale = 1.0
            for _ in range(6):  # Iterative scaling
                fractal += scale * np.sin(xi * scale * 10.0) * np.cos(xi * scale * 5.0)
                scale *= 0.5
                
        # Adaptive gradient field with directional preference
        gradient = 0.0
        for i in range(self.dim):
            # Directional bias based on dimension index
            bias = np.sin(i * np.pi / self.dim) * 0.5 + 0.5
            grad_term = (x[i]**3) * (1.0 + self.adaptation_rate * bias)
            gradient += grad_term
            
        # Multi-scale harmonic interference with varying amplitudes
        harmonic = 0.0
        for i in range(self.dim):
            # Different frequency components
            freqs = [1.0, 2.0, 4.0, 8.0]
            amps = [1.0, 0.7, 0.4, 0.2]
            for f, a in zip(freqs, amps):
                harmonic += a * np.sin(f * x[i]) * np.cos(f * x[i] / 2.0)
                
        # Cross-dimensional coupling with fractal scaling
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = abs(x[i] - x[j])
                # Fractal-like decay
                cross += (1.0 / (1.0 + diff**self.fractal_dim)) * np.sin(diff)
                
        # Non-linear transformation with exponential damping
        transform = 0.0
        for i in range(self.dim):
            # Combine polynomial and exponential terms
            poly_term = x[i]**2 + x[i]**4
            exp_term = np.exp(-0.1 * abs(x[i]))
            transform += poly_term * exp_term
            
        # Add dimension-dependent noise with fractal characteristics
        noise = 0.0
        for i in range(self.dim):
            # Use position-based pseudo-random generator
            seed = int((x[i] * 1000) % 1000)
            np.random.seed(seed)
            local_noise = np.random.uniform(-1, 1)
            noise += local_noise * np.cos(x[i] * 2.0)
            
        # Combine all components with appropriate weights
        result = 0.7 * fractal + 0.8 * gradient + 0.6 * harmonic + 0.4 * cross + 0.3 * transform + 0.2 * noise
        
        # Add offset to ensure global minimum is at origin
        return result + 10.0 * self.dim