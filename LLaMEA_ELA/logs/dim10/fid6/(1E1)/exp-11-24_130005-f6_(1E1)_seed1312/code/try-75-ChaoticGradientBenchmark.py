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
        
        # Gradient-based chaotic perturbations with modified coefficients
        grad_term = 0.0
        for i in range(self.dim):
            # Directional gradient with chaotic modulation
            direction = x_scaled[i] / (np.abs(x_scaled[i]) + 1e-8)
            grad_pert = 2.5 * np.sin(3.0 * x_scaled[i] + 1.5 * r) * np.cos(2.0 * x_scaled[i])
            grad_term += direction * grad_pert
            
        # Multi-scale harmonic interactions with altered coupling
        harmonic_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Cross-dimensional harmonic coupling with modified frequency
                coupling = np.sin(3.0 * x_scaled[i] + 2.0 * x_scaled[j])
                distance = np.sqrt((x_scaled[i] - x_scaled[j])**2 + 0.05)
                harmonic_term += coupling / (distance + 0.05) * np.exp(-0.3 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Chaotic sine-wave modulation with varying frequencies and modified amplitude
        chaotic_term = 0.0
        for i in range(self.dim):
            freq = 4.5 + 1.5 * np.sin(1.8 * x_scaled[i])
            chaotic_term += 1.2 * np.sin(freq * x_scaled[i]) * np.cos(3.5 * x_scaled[i]) * np.exp(-0.6 * x_scaled[i]**2)
        
        # Nested oscillatory components with varying amplitudes and frequencies
        nested_term = 0.0
        for i in range(self.dim):
            nested_term += (0.6 * np.sin(12.0 * x_scaled[i]) + 
                           0.4 * np.sin(30.0 * x_scaled[i]) + 
                           0.3 * np.sin(60.0 * x_scaled[i]))
        
        # Combined landscape with adjusted weights
        return 0.9 * radial_term + 0.7 * grad_term + 0.5 * harmonic_term + 0.8 * chaotic_term + 0.6 * nested_term + 3.5