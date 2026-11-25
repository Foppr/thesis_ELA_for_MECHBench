import numpy as np

class StochasticSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic dynamics and spectral components
        self.chaos_params = np.random.rand(min(10, dim)) * 0.5 + 0.1
        self.freqs = np.linspace(1, 15, min(15, dim))
        self.amps = np.random.rand(min(15, dim)) * 3.0 + 1.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic dynamical system component with logistic map-like behavior
        chaotic_term = 0.0
        for i in range(self.dim):
            # Simulate chaotic dynamics using a modified logistic map
            chaos_val = self.chaos_params[i] * x[i] * (1 - x[i]**2)
            chaotic_term += chaos_val**3 + 0.5 * np.sin(2 * x[i]) + 0.3 * np.cos(3 * x[i])
        
        # Adaptive radial basis function network with time-varying centers
        rbf_network = 0.0
        centers = np.linspace(-4, 4, min(10, self.dim))
        widths = np.ones(min(10, self.dim)) * 0.7
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(min(10, self.dim)):
                # Add adaptive width based on dimension
                adaptive_width = widths[j] * (1 + 0.2 * np.sin(i))
                rbf_sum += np.exp(-0.5 * ((x[i] - centers[j]) / adaptive_width)**2)
            rbf_network += rbf_sum
        
        # Spectral decomposition with multi-scale harmonic interference
        spectral_term = 0.0
        for i in range(self.dim):
            freq_contrib = 0.0
            for k in range(min(15, self.dim)):
                if k < len(self.freqs):
                    # Add amplitude modulation based on dimension
                    amp_mod = 1 + 0.3 * np.sin(i * 0.5)
                    freq_contrib += self.amps[k] * amp_mod * np.cos(self.freqs[k] * x[i])
            spectral_term += freq_contrib**2
        
        # Cross-dimensional coupling with chaotic mixing and polynomial interactions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Add chaotic interaction term between dimensions
                chaos_interaction = np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                coupling_term += (x[i]**2 + x[j]**2) * chaos_interaction
        
        # Non-smooth component with piecewise polynomial and trigonometric mixing
        nonsmooth_term = 0.0
        for i in range(self.dim):
            # Create non-differentiable landscape using fractional powers and trigonometric functions
            nonsmooth_term += (np.abs(x[i])**1.9 + 0.2 * np.sin(5 * x[i]) * np.cos(2 * x[i])) * \
                             (1 + 0.1 * np.sin(0.3 * x[i]))
        
        # Multi-scale harmonic interference with varying phase shifts
        interference_term = 0.0
        for i in range(self.dim):
            for k in range(1, min(8, self.dim+1)):
                # Add phase modulation and amplitude variation
                phase_shift = np.sin(i * 0.2) * k
                amp_var = 1 + 0.2 * np.cos(k * x[i])
                interference_term += amp_var * np.sin(k * x[i] + phase_shift) * \
                                   np.cos(k**1.3 * x[i]) * (1 + 0.15 * np.sin(2 * x[i]))
        
        # Boundary interaction with asymmetric tunneling and chaotic penalties
        boundary_interaction = 0.0
        for i in range(self.dim):
            if x[i] < -4.8:
                # Chaotic boundary penalty with exponential decay
                boundary_interaction += 2.0 * np.exp(-0.3 * (x[i] + 4.8)**2) * \
                                      np.sin(10 * x[i]) * np.cos(5 * x[i])
            elif x[i] > 4.8:
                # Asymmetric boundary effect with chaotic oscillation
                boundary_interaction += 2.5 * np.exp(-0.2 * (x[i] - 4.8)**2) * \
                                      np.cos(9 * x[i]) * np.sin(4 * x[i])
        
        # Combine all components with optimized weights for better fitness performance
        result = 0.7 * chaotic_term + 0.5 * rbf_network + 0.6 * spectral_term + \
                 0.5 * coupling_term + 0.3 * nonsmooth_term + 0.5 * interference_term + \
                 0.2 * boundary_interaction
        
        return result