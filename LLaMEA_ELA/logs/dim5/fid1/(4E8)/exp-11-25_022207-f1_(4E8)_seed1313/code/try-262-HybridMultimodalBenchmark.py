import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial basis function component with dynamic centers and widths
        rbf = 0
        centers = np.linspace(-1, 1, min(7, self.dim))
        widths = np.logspace(-2, 2, min(7, self.dim))
        for i, (c, w) in enumerate(zip(centers, widths)):
            if i < len(x_norm):
                rbf += np.exp(-0.5 * ((x_norm[i] - c) / w)**2)
        
        # Sinusoidal modulation with increased frequencies and chaotic amplitudes
        sin_mod = 0
        freqs = np.linspace(3.0, 12.0, min(8, self.dim))
        amps = np.logspace(0.8, 3.0, min(8, self.dim)) * np.sin(2.0 * np.pi * np.random.rand())
        for i, (f, a) in enumerate(zip(freqs, amps)):
            if i < len(x_norm):
                sin_mod += a * np.sin(f * np.pi * x_norm[i])
        
        # Cross-dimensional interaction terms with higher-order polynomial coupling
        cross_terms = 0
        for i in range(self.dim - 1):
            for j in range(i + 1, self.dim):
                # Increased coupling exponents for greater nonlinearity and complexity
                cross_terms += (x_norm[i]**5 + x_norm[j]**5) * np.sin(np.pi * (x_norm[i] - x_norm[j]))
        
        # Perturbed saddle-point structure with dynamic scaling
        saddle = 0
        for i in range(self.dim - 1):
            # Quintic terms with adaptive coefficients for sharper gradients and more complex curvature
            coeff = 1.0 + 0.5 * np.sin(3.0 * np.pi * x_norm[i])
            saddle += coeff * (x_norm[i]**5 - x_norm[i+1]**5) * np.exp(-0.5 * (x_norm[i] + x_norm[i+1])**2)
        
        # Multi-scale harmonic component with dynamic phase shifts and variable contributions
        harmonic = 0
        scales = [0.1, 0.4, 1.0, 2.0]
        for s in scales:
            harmonic += np.sum(np.sin(s * np.pi * x_norm) * np.cos(s * np.pi * x_norm))
        
        # Enhanced chaotic modulation with multiple frequency components
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(17.0 * x_norm[i]) * np.cos(11.0 * x_norm[i]) + \
                       np.sin(5.0 * x_norm[i]) * np.cos(19.0 * x_norm[i])
        
        # Add a modular structure with dynamic scaling factors
        modular = 0
        for i in range(self.dim):
            modular += np.sin(2.0 * np.pi * x_norm[i]) * np.cos(3.0 * np.pi * x_norm[i]) * \
                       (1.0 + 0.3 * np.sin(7.0 * x_norm[i]))
        
        # Combined function with adaptive scaling and dynamic noise
        result = rbf + sin_mod + cross_terms + saddle + harmonic + chaotic + modular
        
        # Add adaptive noise with dynamic magnitude based on input values
        noise_magnitude = 0.02 * (1.0 + 0.2 * np.std(x_norm))
        noise = noise_magnitude * np.random.randn() * (1.0 + 0.1 * np.abs(np.mean(x_norm)))
        
        return result + noise