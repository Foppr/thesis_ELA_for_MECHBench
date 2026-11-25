import numpy as np

class RotatingEllipticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        
    def f(self, x):
        self.t += 0.02
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced base elliptic quadratic with stronger condition number variation
        condition_number = 50.0 + 450.0 * np.sin(0.3 * self.t)
        base_quadratic = 0.0
        for i in range(self.dim):
            eigenvalue = 1.0 + (condition_number - 1.0) * (i / (self.dim - 1)) if self.dim > 1 else 1.0
            base_quadratic += eigenvalue * x[i]**2
            
        # Enhanced rotating correlation structure with more complex angles
        rotation_angle = 0.8 * np.sin(0.4 * self.t) + 0.3 * np.cos(0.6 * self.t)
        rotated = np.zeros_like(x)
        for i in range(self.dim):
            rotated[i] = x[i] * np.cos(rotation_angle) - x[(i+1) % self.dim] * np.sin(rotation_angle)
            
        # Hybrid perturbations combining trigonometric and hyperbolic components
        trig_perturbation = 0.0
        hyperbolic_perturbation = 0.0
        for i in range(self.dim):
            freq1 = 3.0 + 2.0 * np.sin(0.5 * self.t + i * 0.3)
            amp1 = 0.6 + 0.4 * np.cos(0.6 * self.t + i * 0.4)
            trig_perturbation += amp1 * np.sin(freq1 * rotated[i])
            
            freq2 = 1.5 + 1.0 * np.cos(0.7 * self.t + i * 0.5)
            amp2 = 0.3 + 0.3 * np.sin(0.8 * self.t + i * 0.6)
            hyperbolic_perturbation += amp2 * np.tanh(freq2 * rotated[i])
            
        # Enhanced noise component with dynamic correlation
        noise_intensity = 0.15 + 0.25 * np.sin(0.7 * self.t)
        noise = 0.0
        for i in range(self.dim):
            noise += noise_intensity * np.random.normal(0, 1) * (x[i]**2 + 1) * (0.5 + 0.5 * np.cos(0.9 * self.t + i * 0.2))
            
        # Enhanced saddle-point regions with multiple local minima
        saddle_weight = 0.4 + 0.3 * np.cos(0.8 * self.t)
        saddle_points = 0.0
        for i in range(self.dim):
            saddle_points += saddle_weight * (x[i]**6 - 3*x[i]**4 + 3*x[i]**2)
            
        # Additional coupling terms between variables to increase non-separability
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += 0.1 * np.sin(0.5 * self.t + i * 0.3 + j * 0.4) * x[i] * x[j]
                
        # Combine all components with updated weighting
        w1 = 0.35 + 0.1 * np.sin(0.6 * self.t)
        w2 = 0.3 + 0.15 * np.cos(0.5 * self.t)
        w3 = 0.2 + 0.08 * np.sin(0.7 * self.t)
        w4 = 0.1 + 0.07 * np.cos(0.8 * self.t)
        w5 = 0.05 + 0.03 * np.sin(0.9 * self.t)
        
        result = w1 * base_quadratic + w2 * (trig_perturbation + hyperbolic_perturbation) + w3 * noise + w4 * saddle_points + w5 * coupling_term
        return result