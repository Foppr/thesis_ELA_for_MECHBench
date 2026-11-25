import numpy as np

class ChaoticNestedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with enhanced chaotic modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.2 * r * np.sin(15.0 * r) * np.exp(-0.2 * r)
        
        # Nested sinusoidal components with extremely high frequencies and random amplitudes
        nested_sum = 0.0
        for i in range(self.dim):
            freq = 5.0 * (i + 1) ** 1.5
            amp = 1.0 / ((i + 1) ** 0.8)
            nested_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3) * np.sin(freq * x[i] * 0.7)
        
        # Cross-dimensional coupling with rotational symmetry and chaotic interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Add quaternion-inspired rotational component
                rot_component = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                coupling_term += 0.7 * rot_component
        
        # Polynomial and exponential components with additional chaotic perturbations
        poly_term = np.sum(x**4) * np.cos(0.3 * r) * np.sin(0.2 * r)
        exp_term = np.sum(np.exp(-0.5 * x**2)) * np.sin(0.15 * r) * np.cos(0.1 * r)
        
        # Add a novel chaotic rotational symmetry term
        rot_symmetry = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                angle = np.arctan2(x[j], x[i])
                rot_symmetry += np.sin(3.0 * angle) * np.cos(2.0 * angle) * (x[i]**2 + x[j]**2)
        
        # Final chaotic combination with additional noise factor
        result = radial_term + nested_sum + coupling_term + poly_term + exp_term + 0.1 * rot_symmetry
        
        return result