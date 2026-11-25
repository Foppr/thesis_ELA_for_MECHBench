import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial basis function with chaotic center placement and adaptive widths
        rbf = 0
        centers = np.sin(np.linspace(0, 2*np.pi, min(9, self.dim))) * 0.8
        widths = np.logspace(-1.5, 1.5, min(9, self.dim)) * (1.0 + 0.3 * np.sin(5.0 * np.pi * np.random.rand()))
        for i, (c, w) in enumerate(zip(centers, widths)):
            if i < len(x_norm):
                rbf += np.exp(-0.5 * ((x_norm[i] - c) / w)**2)
        
        # Sinusoidal modulation with chaotic frequencies and dynamic amplitudes
        sin_mod = 0
        freqs = 10.0 + 30.0 * np.random.rand(min(10, self.dim))
        amps = 5.0 + 15.0 * np.random.rand(min(10, self.dim)) * np.cos(7.0 * np.pi * np.random.rand())
        for i, (f, a) in enumerate(zip(freqs, amps)):
            if i < len(x_norm):
                sin_mod += a * np.sin(f * x_norm[i] + 0.5 * np.sin(11.0 * x_norm[i]))
        
        # Cross-dimensional interaction terms with dynamic coupling and chaotic exponents
        cross_terms = 0
        for i in range(self.dim - 1):
            for j in range(i + 1, self.dim):
                # Dynamic exponents based on input values for non-uniform coupling
                exp_i = 5.0 + 4.0 * np.sin(2.0 * x_norm[i])
                exp_j = 5.0 + 4.0 * np.cos(2.0 * x_norm[j])
                cross_terms += (x_norm[i]**exp_i + x_norm[j]**exp_j) * np.sin(np.pi * (x_norm[i] - x_norm[j]) * (1.0 + 0.2 * np.sin(3.0 * x_norm[i])))
        
        # Perturbed saddle-point structure with dynamic scaling and chaotic coefficients
        saddle = 0
        for i in range(self.dim - 1):
            # Chaotic quintic terms with time-varying coefficients
            coeff_i = 1.5 + 0.8 * np.sin(7.0 * x_norm[i] + 2.0 * np.pi * np.random.rand())
            coeff_j = 1.5 + 0.8 * np.cos(7.0 * x_norm[i+1] + 2.0 * np.pi * np.random.rand())
            saddle += coeff_i * (x_norm[i]**9 - x_norm[i+1]**9) * np.exp(-0.5 * (x_norm[i] + x_norm[i+1])**3)
        
        # Multi-scale harmonic component with chaotic phase shifts and variable contributions
        harmonic = 0
        scales = [0.2, 0.6, 1.2, 2.4, 4.8]
        for s in scales:
            harmonic += np.sum(np.sin(s * x_norm + 0.3 * np.sin(17.0 * x_norm)) * np.cos(s * x_norm + 0.3 * np.cos(19.0 * x_norm)))
        
        # Enhanced chaotic modulation with multiple frequency components and dynamic coupling
        chaotic = 0
        for i in range(self.dim):
            chaotic += (np.sin(23.0 * x_norm[i]) * np.cos(17.0 * x_norm[i]) + 
                       np.sin(11.0 * x_norm[i]) * np.cos(29.0 * x_norm[i])) * (1.0 + 0.5 * np.sin(13.0 * x_norm[i]))
        
        # Modular structure with dynamic scaling and chaotic perturbations
        modular = 0
        for i in range(self.dim):
            modular += np.sin(3.0 * x_norm[i]) * np.cos(4.0 * x_norm[i]) * \
                       (1.0 + 0.4 * np.sin(11.0 * x_norm[i] + 0.7 * np.pi * np.random.rand()))
        
        # Combined function with chaotic scaling and dynamic noise
        result = rbf + sin_mod + cross_terms + saddle + harmonic + chaotic + modular
        
        # Add adaptive noise with chaotic magnitude and dynamic phase
        noise_magnitude = 0.05 * (1.0 + 0.3 * np.std(x_norm)) * (1.0 + 0.2 * np.sin(19.0 * np.mean(x_norm)))
        noise_phase = 0.5 * np.pi * np.random.rand()
        noise = noise_magnitude * np.random.randn() * (1.0 + 0.15 * np.abs(np.mean(x_norm)) * np.cos(noise_phase))
        
        return result + noise