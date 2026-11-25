import numpy as np

class StochasticSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute some constants for spectral decomposition
        self.freqs = np.linspace(1, 10, min(10, dim))
        self.amps = np.random.rand(min(10, dim)) * 2.0 + 1.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Stochastic differential equation component with Brownian motion-like behavior
        stochastic_term = 0.0
        for i in range(self.dim):
            # Simulate a noisy gradient descent component
            noise = np.random.normal(0, 0.1)
            stochastic_term += (x[i]**3 - 3*x[i]) * np.exp(-0.1 * x[i]**2) + noise
        
        # Radial basis function network with adaptive centers and widths
        rbf_network = 0.0
        centers = np.linspace(-4, 4, min(8, self.dim))
        widths = np.ones(min(8, self.dim)) * 0.5
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(min(8, self.dim)):
                rbf_sum += np.exp(-0.5 * ((x[i] - centers[j]) / widths[j])**2)
            rbf_network += rbf_sum
        
        # Spectral decomposition component using discrete cosine transform-like terms
        spectral_term = 0.0
        for i in range(self.dim):
            freq_contrib = 0.0
            for k in range(min(10, self.dim)):
                if k < len(self.freqs):
                    freq_contrib += self.amps[k] * np.cos(self.freqs[k] * x[i])
            spectral_term += freq_contrib**2
        
        # Cross-dimensional coupling with polynomial interactions and trigonometric mixing
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += (x[i]**2 + x[j]**2) * np.sin(0.5 * (x[i] - x[j])) * np.cos(0.3 * (x[i] + x[j]))
        
        # Non-smooth component with absolute value and step function behavior
        nonsmooth_term = 0.0
        for i in range(self.dim):
            # Create a non-differentiable landscape using absolute values and step functions
            nonsmooth_term += np.abs(x[i])**1.5 + 0.3 * np.sin(10 * x[i]) * np.cos(5 * x[i])
        
        # Multi-scale harmonic interference with varying amplitudes and frequencies
        interference_term = 0.0
        for i in range(self.dim):
            for k in range(1, min(6, self.dim+1)):
                interference_term += np.sin(k * x[i]) * np.cos(k**1.5 * x[i]) * (1 + 0.2 * np.sin(3 * x[i]))
        
        # Boundary interaction with asymmetric penalty and tunneling effect
        boundary_interaction = 0.0
        for i in range(self.dim):
            if x[i] < -4.5:
                boundary_interaction += 3.0 * np.exp(-0.2 * (x[i] + 4.5)**2) * np.sin(8 * x[i])
            elif x[i] > 4.5:
                boundary_interaction += 2.5 * np.exp(-0.15 * (x[i] - 4.5)**2) * np.cos(7 * x[i])
        
        # Combine all components with carefully tuned weights
        result = 0.8 * stochastic_term + 0.6 * rbf_network + 0.7 * spectral_term + \
                 0.5 * coupling_term + 0.4 * nonsmooth_term + 0.6 * interference_term + \
                 0.3 * boundary_interaction
        
        return result