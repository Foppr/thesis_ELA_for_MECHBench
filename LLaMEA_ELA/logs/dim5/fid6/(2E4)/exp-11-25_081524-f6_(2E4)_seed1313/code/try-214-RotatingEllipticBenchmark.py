import numpy as np

class RotatingEllipticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        
    def f(self, x):
        self.t += 0.02
        x = np.clip(x, -5.0, 5.0)
        
        # Base elliptic quadratic with time-varying condition number
        condition_number = 100.0 + 900.0 * np.sin(0.3 * self.t)
        base_quadratic = 0.0
        for i in range(self.dim):
            # Varying eigenvalues with time
            eigenvalue = 1.0 + (condition_number - 1.0) * (i / (self.dim - 1)) if self.dim > 1 else 1.0
            base_quadratic += eigenvalue * x[i]**2
            
        # Rotating correlation structure with dynamic angles
        rotation_angle = 0.5 * np.sin(0.4 * self.t)
        rotated = np.zeros_like(x)
        for i in range(self.dim):
            rotated[i] = x[i] * np.cos(rotation_angle) - x[(i+1) % self.dim] * np.sin(rotation_angle)
            
        # Trigonometric perturbations with varying frequencies and amplitudes
        trig_perturbation = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.5 * self.t + i * 0.3)
            amp = 0.5 + 0.5 * np.cos(0.6 * self.t + i * 0.4)
            trig_perturbation += amp * np.sin(freq * rotated[i])
            
        # Adaptive noise component with time-varying intensity
        noise_intensity = 0.1 + 0.2 * np.sin(0.7 * self.t)
        noise = 0.0
        for i in range(self.dim):
            noise += noise_intensity * np.random.normal(0, 1) * (x[i]**2 + 1)
            
        # Dynamic saddle-point regions with time-varying weights
        saddle_weight = 0.3 + 0.2 * np.cos(0.8 * self.t)
        saddle_points = 0.0
        for i in range(self.dim):
            saddle_points += saddle_weight * x[i]**4 - 2 * x[i]**2
            
        # Combine all components with adaptive weighting
        w1 = 0.4 + 0.1 * np.sin(0.6 * self.t)
        w2 = 0.3 + 0.15 * np.cos(0.5 * self.t)
        w3 = 0.2 + 0.05 * np.sin(0.7 * self.t)
        w4 = 0.1 + 0.05 * np.cos(0.8 * self.t)
        
        result = w1 * base_quadratic + w2 * trig_perturbation + w3 * noise + w4 * saddle_points
        return result