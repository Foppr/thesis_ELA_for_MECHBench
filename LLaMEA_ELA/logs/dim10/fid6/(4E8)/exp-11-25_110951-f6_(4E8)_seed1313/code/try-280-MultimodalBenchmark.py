import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal-like multimodal structure with self-similar properties
        fractal_term = 0.0
        for i in range(self.dim):
            # Multi-scale sinusoidal modulations with varying frequencies
            scale1 = np.sin(2 * np.pi * x_norm[i])
            scale2 = np.sin(4 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i])
            scale3 = np.sin(8 * np.pi * x_norm[i]) * np.cos(7 * np.pi * x_norm[i]) * np.sin(5 * np.pi * x_norm[i])
            fractal_term += scale1**2 + 0.5 * scale2**2 + 0.3 * scale3**2
        
        # Log-periodic oscillations with varying amplitudes and frequencies
        log_oscillation = 0.0
        for i in range(self.dim):
            # Apply log-periodic modulation with chaotic perturbation
            log_freq = 10**(1 + 0.5 * np.sin(x_norm[i]))
            log_amp = 2 + np.cos(3 * x_norm[i]) * np.sin(7 * x_norm[i])
            log_oscillation += log_amp * np.sin(log_freq * x_norm[i]) * np.exp(-0.1 * x_norm[i]**2)
        
        # Gradient-based attraction basins with varying strengths
        gradient_basin = 0.0
        for i in range(self.dim):
            # Create multiple local minima with different basin characteristics
            basin1 = (x_norm[i] - 0.5)**2 * np.exp(-0.5 * (x_norm[i] - 0.5)**2)
            basin2 = (x_norm[i] + 0.3)**2 * np.exp(-0.3 * (x_norm[i] + 0.3)**2)
            basin3 = x_norm[i]**4 * np.exp(-0.2 * x_norm[i]**2)
            gradient_basin += basin1 + 0.7 * basin2 + 0.5 * basin3
        
        # Cross-dimensional interaction terms with asymmetric coupling
        cross_term = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 2) % self.dim
            # Asymmetric elliptic structure with cross-dimensional coupling
            cross_term += (x_norm[i]**2 + 0.3 * x_norm[j]**2 + 0.2 * x_norm[k]**2) * \
                         np.sin(2 * np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[j]) * \
                         np.exp(-0.1 * (x_norm[i] - x_norm[j])**2)
        
        # Multi-scale exponential potentials with chaotic modulation
        exp_potential = 0.0
        for i in range(self.dim):
            exp_potential += np.exp(-np.abs(x_norm[i])) * (1 + 0.5 * np.sin(3 * x_norm[i]) + 
                                                          0.3 * np.sin(7 * x_norm[i]) * np.cos(11 * x_norm[i]))
        
        # Add spectral complexity through harmonic interference
        spectral_term = 0.0
        for i in range(self.dim):
            spectral_term += (np.sin(15 * x_norm[i]) * np.cos(12 * x_norm[i]) + 
                            0.7 * np.sin(25 * x_norm[i])**2 * np.cos(20 * x_norm[i]))
        
        # Combine all terms with appropriate weights
        return (0.3 * fractal_term + 0.25 * log_oscillation + 0.2 * gradient_basin + 
                0.1 * cross_term + 0.1 * exp_potential + 0.05 * spectral_term)