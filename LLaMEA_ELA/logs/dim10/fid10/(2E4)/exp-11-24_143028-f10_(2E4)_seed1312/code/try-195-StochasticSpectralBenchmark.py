import numpy as np

class StochasticSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic dynamics and spectral components
        self.chaos_params = np.random.rand(min(10, dim)) * 0.5 + 0.1
        self.freqs = np.linspace(1, 20, min(20, dim))
        self.amps = np.random.rand(min(20, dim)) * 4.0 + 1.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic dynamical system component with logistic map-like behavior
        chaotic_term = 0.0
        for i in range(self.dim):
            # Simulate chaotic dynamics using a modified logistic map with higher-order terms
            chaos_val = self.chaos_params[i] * x[i] * (1 - x[i]**2) + 0.1 * x[i]**3
            chaotic_term += chaos_val**4 + 0.6 * np.sin(2 * x[i]) + 0.4 * np.cos(3 * x[i]) + 0.2 * np.tan(0.5 * x[i])
        
        # Adaptive radial basis function network with time-varying centers and fractal modulation
        rbf_network = 0.0
        centers = np.linspace(-4, 4, min(12, self.dim))
        widths = np.ones(min(12, self.dim)) * 0.8
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(min(12, self.dim)):
                # Add adaptive width based on dimension with fractal scaling
                adaptive_width = widths[j] * (1 + 0.3 * np.sin(i * 0.7) * np.cos(j * 0.4))
                rbf_sum += np.exp(-0.5 * ((x[i] - centers[j]) / adaptive_width)**2)
            rbf_network += rbf_sum
        
        # Spectral decomposition with multi-scale harmonic interference and fractal frequency modulation
        spectral_term = 0.0
        for i in range(self.dim):
            freq_contrib = 0.0
            for k in range(min(20, self.dim)):
                if k < len(self.freqs):
                    # Add amplitude modulation based on dimension with fractal scaling
                    amp_mod = 1 + 0.4 * np.sin(i * 0.6) * np.cos(k * 0.3)
                    freq_contrib += self.amps[k] * amp_mod * np.cos(self.freqs[k] * x[i] + 0.2 * np.sin(k * x[i]))
            spectral_term += freq_contrib**3
        
        # Cross-dimensional coupling with chaotic mixing and higher-order polynomial interactions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Add chaotic interaction term between dimensions with fractal modulation
                chaos_interaction = np.sin(x[i] * x[j]) * np.exp(-0.15 * (x[i]**2 + x[j]**2)) + 0.1 * np.cos(x[i] + x[j])**3
                coupling_term += (x[i]**3 + x[j]**3) * chaos_interaction
        
        # Non-smooth component with piecewise polynomial and trigonometric mixing, enhanced with fractal scaling
        nonsmooth_term = 0.0
        for i in range(self.dim):
            # Create non-differentiable landscape using fractional powers and trigonometric functions with fractal modulation
            nonsmooth_term += (np.abs(x[i])**2.1 + 0.3 * np.sin(6 * x[i]) * np.cos(3 * x[i]) + 0.1 * np.tan(0.4 * x[i])) * \
                             (1 + 0.15 * np.sin(0.4 * x[i]) * np.cos(0.3 * x[i]))
        
        # Multi-scale harmonic interference with varying phase shifts and fractal amplitude modulation
        interference_term = 0.0
        for i in range(self.dim):
            for k in range(1, min(10, self.dim+1)):
                # Add phase modulation and amplitude variation with fractal scaling
                phase_shift = np.sin(i * 0.3) * k + 0.2 * np.cos(k * x[i])
                amp_var = 1 + 0.3 * np.cos(k * x[i]) * np.sin(i * 0.5)
                interference_term += amp_var * np.sin(k * x[i] + phase_shift) * \
                                   np.cos(k**1.5 * x[i]) * (1 + 0.2 * np.sin(3 * x[i]) * np.cos(2 * x[i]))
        
        # Boundary interaction with asymmetric tunneling, chaotic penalties and fractal boundary scaling
        boundary_interaction = 0.0
        for i in range(self.dim):
            if x[i] < -4.9:
                # Chaotic boundary penalty with exponential decay and fractal scaling
                boundary_interaction += 2.5 * np.exp(-0.35 * (x[i] + 4.9)**2) * \
                                      np.sin(12 * x[i]) * np.cos(6 * x[i]) + 0.2 * np.tan(0.3 * x[i])
            elif x[i] > 4.9:
                # Asymmetric boundary effect with chaotic oscillation and fractal modulation
                boundary_interaction += 3.0 * np.exp(-0.25 * (x[i] - 4.9)**2) * \
                                      np.cos(11 * x[i]) * np.sin(5 * x[i]) + 0.1 * np.sin(0.5 * x[i])
        
        # Combine all components with optimized weights for better fitness performance
        result = 0.8 * chaotic_term + 0.6 * rbf_network + 0.7 * spectral_term + \
                 0.6 * coupling_term + 0.4 * nonsmooth_term + 0.6 * interference_term + \
                 0.3 * boundary_interaction
        
        return result