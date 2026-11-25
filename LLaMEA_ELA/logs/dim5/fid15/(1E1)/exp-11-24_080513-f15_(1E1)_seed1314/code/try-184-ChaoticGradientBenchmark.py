import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced chaotic component with fractional Brownian motion-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            # Simulate fractional Brownian motion using cumulative sine waves
            fbm_val = 0.0
            for k in range(1, 8):
                fbm_val += (1.0/k) * np.sin(k * x_normalized[i] * 10.0)
            chaotic += np.sin(fbm_val * 5.0) * np.cos(fbm_val * 3.0)
        
        # Gradient-based component with variable conditioning and exponential scaling
        gradient = 0.0
        for i in range(self.dim):
            condition = 1.0 + 5.0 * np.sin(i * 0.5) * np.cos(i * 0.3)
            gradient += condition * (x_normalized[i] ** 4) * np.exp(-0.2 * x_normalized[i]**2)
        
        # Enhanced saddle point region with polynomial coupling and sign changes
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended coupling
                term = (x_normalized[i] ** 2 - x_normalized[j] ** 2) * np.sin(x_normalized[i] * x_normalized[j])
                saddle += term * np.exp(-0.5 * (x_normalized[i] - x_normalized[j])**2)
        
        # Novel discontinuity mechanism using fractional Laplace-like operators
        discontinuous = 0.0
        for i in range(self.dim):
            # Fractional-like behavior with power-law decay
            frac_val = np.sign(x_normalized[i]) * np.abs(x_normalized[i]) ** 0.7
            discontinuous += frac_val * np.sin(5 * x_normalized[i]) * np.cos(3 * x_normalized[i])
        
        # Multi-scale harmonic interaction with adaptive weights and phase shifts
        harmonic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_normalized[i] - x_normalized[j])
                weight = np.exp(-dist * 3.0) * (1.0 + 0.5 * np.sin(dist * 2.0))
                phase = np.sin(i * 0.5) * np.cos(j * 0.3)
                harmonic += weight * np.sin(4 * (x_normalized[i] + x_normalized[j]) + phase) * np.cos(4 * (x_normalized[i] - x_normalized[j]))
        
        # Multi-modal nonlinearity with multiple peaks and valleys
        nonlin = 0.0
        for i in range(self.dim):
            # Multiple sinusoidal modulations creating multi-modal landscape
            modal_val = (x_normalized[i]**2) * np.sin(x_normalized[i])**2 + 0.5 * (x_normalized[i]**3) * np.cos(x_normalized[i])
            nonlin += modal_val
        
        # Combined fitness with new scaling factors and added noise component
        noise = 0.01 * np.sum(np.random.randn(self.dim) * x_normalized)
        
        return (0.28 * chaotic + 0.22 * gradient + 0.18 * saddle + 
                0.17 * discontinuous + 0.12 * harmonic + 0.03 * nonlin + noise)