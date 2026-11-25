import numpy as np

class RotatingEllipticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        
    def f(self, x):
        self.t += 0.03
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic base with exponential condition number variation
        condition_number = 1000.0 * np.exp(0.02 * np.sin(0.5 * self.t)) + 100.0
        base_quadratic = 0.0
        for i in range(self.dim):
            eigenvalue = (1.0 + (condition_number - 1.0) * (i / (self.dim - 1))) if self.dim > 1 else 1.0
            base_quadratic += eigenvalue * x[i]**2
            
        # Non-separable correlation with chaotic rotation angles
        rotation_angle = 0.8 * np.sin(0.6 * self.t + 0.3 * np.sum(x))
        rotated = np.zeros_like(x)
        for i in range(self.dim):
            rotated[i] = x[i] * np.cos(rotation_angle) - x[(i+1) % self.dim] * np.sin(rotation_angle)
            
        # Multi-frequency trigonometric perturbations with chaotic amplitudes
        trig_perturbation = 0.0
        for i in range(self.dim):
            freq = 3.0 + 4.0 * np.sin(0.7 * self.t + i * 0.5)
            amp = 1.0 + 0.8 * np.sin(0.9 * self.t + i * 0.6)
            trig_perturbation += amp * np.sin(freq * rotated[i]) * np.cos(freq * rotated[(i+2) % self.dim])
            
        # Enhanced noise with chaotic intensity and dynamic correlation
        noise_intensity = 0.3 + 0.4 * np.sin(0.8 * self.t + np.sum(x))
        noise = 0.0
        for i in range(self.dim):
            noise += noise_intensity * np.random.normal(0, 1) * (x[i]**2 + 1) * np.cos(0.5 * self.t + i * 0.3)
            
        # Complex saddle-point regions with chaotic weights and multiple dimensions
        saddle_weight = 0.5 + 0.3 * np.sin(0.9 * self.t + np.sum(x))
        saddle_points = 0.0
        for i in range(self.dim):
            saddle_points += saddle_weight * (x[i]**6 - 3 * x[i]**4 + 3 * x[i]**2)
            
        # Dynamic coupling between components with time-varying interaction coefficients
        coupling_coeff = 0.2 + 0.1 * np.sin(0.4 * self.t + np.sum(x))
        coupling_terms = 0.0
        for i in range(self.dim):
            coupling_terms += coupling_coeff * x[i] * x[(i+1) % self.dim]
            
        # Combine all components with chaotic weighting factors
        w1 = 0.3 + 0.2 * np.sin(0.7 * self.t)
        w2 = 0.25 + 0.15 * np.cos(0.6 * self.t + np.sum(x))
        w3 = 0.2 + 0.1 * np.sin(0.8 * self.t)
        w4 = 0.15 + 0.05 * np.cos(0.9 * self.t + np.sum(x))
        w5 = 0.1 + 0.05 * np.sin(0.5 * self.t)
        
        result = w1 * base_quadratic + w2 * trig_perturbation + w3 * noise + w4 * saddle_points + w5 * coupling_terms
        return result