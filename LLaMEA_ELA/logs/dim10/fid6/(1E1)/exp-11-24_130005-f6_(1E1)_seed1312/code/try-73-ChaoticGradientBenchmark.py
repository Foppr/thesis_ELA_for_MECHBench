import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with harmonic modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = r * (1.0 + 0.3 * np.sin(5.0 * r) + 0.2 * np.cos(7.0 * r))
        
        # Gradient-based chaotic perturbations
        grad_term = 0.0
        for i in range(self.dim):
            # Directional gradient with chaotic modulation
            direction = x_scaled[i] / (np.abs(x_scaled[i]) + 1e-8)
            grad_pert = 2.0 * np.sin(3.0 * x_scaled[i] + 1.5 * r) * np.cos(2.0 * x_scaled[i])
            grad_term += direction * grad_pert
            
        # Multi-scale harmonic interactions
        harmonic_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Cross-dimensional harmonic coupling
                coupling = np.sin(2.5 * x_scaled[i] + 1.8 * x_scaled[j])
                distance = np.sqrt((x_scaled[i] - x_scaled[j])**2 + 0.1)
                harmonic_term += coupling / (distance + 0.1) * np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Chaotic sine-wave modulation with varying frequencies
        chaotic_term = 0.0
        for i in range(self.dim):
            freq = 4.0 + 2.0 * np.sin(1.5 * x_scaled[i])
            chaotic_term += np.sin(freq * x_scaled[i]) * np.cos(3.0 * x_scaled[i]) * np.exp(-0.5 * x_scaled[i]**2)
        
        # Nested oscillatory components with varying amplitudes
        nested_term = 0.0
        for i in range(self.dim):
            nested_term += (0.5 * np.sin(10.0 * x_scaled[i]) + 
                           0.3 * np.sin(25.0 * x_scaled[i]) + 
                           0.2 * np.sin(50.0 * x_scaled[i]))
        
        # Combined landscape with adaptive weights
        return 0.8 * radial_term + 0.6 * grad_term + 0.4 * harmonic_term + 0.7 * chaotic_term + 0.5 * nested_term + 3.0