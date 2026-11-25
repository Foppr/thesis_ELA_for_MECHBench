import numpy as np

class TrigonometricModulationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.frequency_modulation = np.random.uniform(0.5, 2.0, dim)
        self.coupling_strength = np.random.uniform(0.3, 1.5, dim)
        self.rotation_angles = np.random.uniform(-np.pi, np.pi, dim)
        self.penalty_weights = np.random.uniform(1.0, 3.0, dim)
        self.adaptive_scaling = np.random.uniform(0.8, 1.2, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Base trigonometric component with frequency modulation
        trig_term = 0.0
        for i in range(self.dim):
            freq = self.frequency_modulation[i] * (1.0 + 0.2 * np.sin(i * 0.7))
            trig_term += (np.sin(freq * x[i]) + np.cos(freq * x[i])) * np.exp(-0.1 * np.abs(x[i]))
            
        # Directional coupling with rotation effects
        coupling_term = 0.0
        for i in range(self.dim):
            rotated_x = x[i] * np.cos(self.rotation_angles[i]) - x[(i+1) % self.dim] * np.sin(self.rotation_angles[i])
            coupling_term += self.coupling_strength[i] * np.sin(2.0 * rotated_x) * np.cos(0.5 * x[i])
            
        # Adaptive scaling component with dynamic penalty
        scaling_term = 0.0
        for i in range(self.dim):
            scale_factor = self.adaptive_scaling[i] * (1.0 + 0.3 * np.cos(i * 0.4))
            penalty = self.penalty_weights[i] * (np.exp(-0.5 * (x[i] - 2.0)**2) + np.exp(-0.5 * (x[i] + 2.0)**2))
            scaling_term += scale_factor * x[i]**2 * np.sin(0.3 * x[i]) + penalty
            
        # Cross-dimensional interaction with multi-scale modulation
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + (x[(i+1) % self.dim] - x[(j+1) % self.dim])**2)
                modulation = np.sin(0.5 * dist) * np.cos(0.3 * dist)
                cross_term += modulation * (1.0 + 0.2 * np.sin(i * j * 0.1))
                
        # Multi-modal structure with dynamic barrier
        modal_term = 0.0
        for i in range(self.dim):
            # Create multiple local minima using sinusoidal modulation
            modal_term += (np.sin(3.0 * x[i]) + np.cos(2.0 * x[i])) * np.exp(-0.2 * x[i]**2)
            
        # Combined fitness with adaptive weighting
        total = 0.7 * trig_term + 0.6 * coupling_term + 0.8 * scaling_term + 0.5 * cross_term + 0.9 * modal_term
        
        return total