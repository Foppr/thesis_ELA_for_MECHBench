import numpy as np

class FractalPhaseTransitionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_dimension = 1.5 + np.random.rand() * 0.5
        self.phase_transition_freq = 0.5 + np.random.rand() * 2.0
        self.geometry_scale = 2.0 + np.random.rand() * 3.0
        self.transition_strength = 0.8 + np.random.rand() * 0.4
        self.roughness = 0.3 + np.random.rand() * 0.7
        self.rotation_angles = np.random.uniform(0, 2*np.pi, dim)
        self.translation_offsets = np.random.uniform(-1.0, 1.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize coordinates to [-1, 1] for fractal generation
        x_norm = x / 5.0
        
        # Apply rotation and translation
        x_rot = np.zeros_like(x_norm)
        for i in range(self.dim):
            angle = self.rotation_angles[i]
            if self.dim > 1:
                cos_a, sin_a = np.cos(angle), np.sin(angle)
                x_rot[i] = x_norm[i] * cos_a - x_norm[(i+1) % self.dim] * sin_a
            else:
                x_rot[i] = x_norm[i]
        
        # Fractal-based multimodal structure using recursive pattern
        fractal_value = 0.0
        scale_factor = 1.0
        for depth in range(3):
            if depth > 0:
                scale_factor *= 0.5
            
            # Generate fractal pattern with self-similarity
            pattern = np.zeros(self.dim)
            for i in range(self.dim):
                pattern[i] = np.sin(scale_factor * (x_rot[i] + self.translation_offsets[i]) * 
                                  (2 ** depth) * self.geometry_scale)
            
            # Combine with phase transition dynamics
            phase_term = np.sin(self.phase_transition_freq * depth)
            fractal_value += scale_factor * phase_term * np.sum(pattern**2)
        
        # Phase transition modulation creating dynamic curvature
        transition_mod = 1.0 + self.transition_strength * np.sin(
            np.sum(x_rot) * self.phase_transition_freq)
        
        # Add roughness through noise and higher-order terms
        noise = np.random.normal(0, self.roughness)
        curvature_term = np.sum(x_rot**4) * 0.1
        
        result = transition_mod * fractal_value + curvature_term + noise
        
        return result