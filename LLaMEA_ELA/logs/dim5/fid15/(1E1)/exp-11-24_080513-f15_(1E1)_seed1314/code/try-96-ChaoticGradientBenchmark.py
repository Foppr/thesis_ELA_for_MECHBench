import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute harmonic coefficients for stability
        self.coeffs = np.array([np.sin(i * 0.3) * np.cos(i * 0.4) for i in range(dim)])
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic dynamics component with delayed feedback
        chaotic = 0.0
        delay = 2
        for i in range(self.dim):
            # Time-delayed chaotic map with varying coupling strength
            if i >= delay:
                feedback = x_norm[i - delay]
            else:
                feedback = 0.0
                
            # Logistic-like chaotic behavior with harmonic modulation
            r = 3.8 + 0.2 * np.sin(i * 0.5)
            chaotic += (r * x_norm[i] * (1 - x_norm[i]) + 
                       0.1 * feedback * np.cos(2 * np.pi * x_norm[i])) ** 2
        
        # Multi-scale harmonic modulation with varying frequencies and amplitudes
        harmonic = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.7)
            amp = 1.0 + 0.5 * np.cos(i * 0.3)
            phase = 0.5 * np.sin(i * 0.9)
            harmonic += amp * np.sin(freq * x_norm[i] + phase) * np.cos(freq * x_norm[i] + phase)
        
        # Gradient-based interaction with non-linear coupling
        gradient = 0.0
        for i in range(self.dim):
            grad_term = 0.0
            for j in range(self.dim):
                if i != j:
                    # Non-linear coupling with distance-dependent strength
                    dist = np.abs(x_norm[i] - x_norm[j])
                    coupling_strength = 1.0 / (1.0 + dist**2)
                    grad_term += coupling_strength * np.sin(3 * (x_norm[i] - x_norm[j]))
            gradient += grad_term ** 2
        
        # Multi-scale periodic potential with exponential decay
        potential = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(i * 0.4)
            period = 2.0 + 0.3 * np.cos(i * 0.6)
            # Create periodic wells with varying depths
            potential += scale * np.exp(-0.5 * ((x_norm[i] - np.sin(i * 0.2)) / (0.1 + 0.2 * np.abs(x_norm[i])))**2) * \
                        np.cos(period * x_norm[i])
        
        # Cross-dimensional coupling with time-varying coefficients
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Time-varying coupling coefficient
                coeff = 0.5 + 0.5 * np.sin(0.3 * (i + j))
                cross += coeff * np.sin(2 * (x_norm[i] - x_norm[j])) * \
                        np.exp(-0.1 * (x_norm[i] - x_norm[j])**2)
        
        # Logarithmic spiral component with complex phase
        spiral = 0.0
        for i in range(self.dim):
            r = np.sqrt(x_norm[i]**2 + 0.1)
            theta = np.arctan2(x_norm[i], 0.1) + 0.3 * i
            # Spiral pattern with varying amplitude and frequency
            spiral += r * np.sin(5 * theta + 0.5 * np.cos(i * 0.7)) * \
                     np.exp(-0.2 * r**2)
        
        # Combine all components with adaptive weights
        return (0.25 * chaotic + 0.2 * harmonic + 0.15 * gradient + 
                0.15 * potential + 0.15 * cross + 0.1 * spiral)