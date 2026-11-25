import numpy as np

class QuantumFractalGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Quantum-inspired probability distribution component
        quantum_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Superposition of quantum-like probability amplitudes with phase modulation
            phase = np.pi * (i + 1) * np.sum(x_norm[:i+1]) / self.dim if i > 0 else 0
            amplitude = 1.0 + 0.3 * np.sin(xi * 5 + phase)
            probability = amplitude**2
            quantum_component += probability * (1.0 + 0.2 * np.cos(i * np.pi / self.dim))
        
        # Fractal Brownian motion component with Hurst parameter modulation
        fbm_component = 0
        hurst_params = np.linspace(0.3, 0.8, self.dim)
        for i in range(self.dim):
            xi = x_norm[i]
           hurst = hurst_params[i]
            # Fractal Brownian motion with dimension-dependent Hurst parameter
            fbm_value = np.sin(xi * (2**i)) * (1.0 + 0.1 * np.cos(xi * 3))
            fbm_component += fbm_value * (1.0 + 0.25 * hurst * np.sin(i * np.pi / self.dim))
        
        # Adaptive gradient field with spectral coupling
        gradient_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Adaptive scaling based on local curvature and dimension position
            scale_factor = 1.0 + 0.5 * np.cos(i * np.pi / self.dim) * (1.0 + 0.2 * xi**2)
            gradient_component += scale_factor * (xi**4 - 2*xi**2 + 0.5) * \
                                (1.0 + 0.1 * np.sin(i * np.pi / self.dim)) + \
                                0.3 * np.cos(xi * 7) * np.sin(i)
        
        # Cross-dimensional spectral coupling with quantum interference
        coupling_component = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Quantum interference pattern with dimension-dependent phase
                phase_diff = (i - j) * np.pi / self.dim
                coupling_strength = 1.0 + 0.3 * np.cos(phase_diff)
                coupling_component += coupling_strength * np.sin(x_norm[i] * x_norm[j]) * \
                                    np.cos(x_norm[i] + x_norm[j]) * \
                                    (1.0 + 0.15 * np.sin(i + j))
        
        # Multi-scale fractal modulation with quantum tunneling effects
        fractal_component = 0
        scales = [1, 2, 4, 8]
        for i in range(self.dim):
            xi = x_norm[i]
            for k, scale in enumerate(scales):
                # Fractal with quantum-like tunneling probability
                tunnel_prob = 1.0 / (1.0 + np.exp(-scale * (xi - 0.5)))
                fractal_component += tunnel_prob * np.sin(scale * xi) * \
                                   (1.0 + 0.1 * np.cos(i * scale))
        
        # Dynamic dimensionality scaling with spectral weighting
        spectral_weights = np.array([1.0, 1.2, 1.4, 1.6, 1.8])
        if self.dim >= 5:
            weights = spectral_weights[:self.dim]
        else:
            weights = np.tile(spectral_weights, (self.dim // 5) + 1)[:self.dim]
        
        # Combine all components with dynamic weights
        result = (weights[0] * quantum_component + 
                 weights[1] * fbm_component + 
                 weights[2] * gradient_component + 
                 weights[3] * coupling_component + 
                 weights[4] * fractal_component)
        
        # Add adaptive noise with quantum-inspired complexity
        noise_amplitude = 0.02 * (1 + 0.02 * np.abs(result)) * \
                         (1 + 0.03 * np.sum(np.abs(x_norm))) * \
                         (1 + 0.05 * np.cos(np.sum(x_norm) * 2))
        noise = np.random.normal(0, noise_amplitude)
        
        return result + noise