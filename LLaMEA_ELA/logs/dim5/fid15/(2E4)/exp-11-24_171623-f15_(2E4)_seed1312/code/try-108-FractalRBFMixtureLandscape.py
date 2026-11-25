import numpy as np

class FractalRBFMixtureLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial Basis Function components with fractal scaling and quaternion-inspired symmetry
        rbf_sum = 0
        centers = np.linspace(-1, 1, min(25, self.dim * 3))
        for i in range(len(centers)):
            if i < self.dim:
                distance = np.sum((x_norm - centers[i])**2)
                rbf_sum += np.exp(-7 * distance) * np.sin(4 * np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[i])
        
        # Sine-wave modulation with chaotic frequency coupling and rotational symmetry
        sine_mod = 0
        for i in range(self.dim):
            freq = 3 + 2 * np.sin(x_norm[i] * np.pi / 3) + 0.5 * np.cos(x_norm[i] * np.pi)
            sine_mod += np.sin(freq * x_norm[i]) * np.cos(2 * x_norm[i]) * np.sin(x_norm[i]**2)
        
        # Fractal-like coupling with recursive interaction terms and rotational invariance
        fractal_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                fractal_term += (np.sin(15 * dist) / (dist + 0.05)) * np.exp(-dist**3) * np.cos(dist * np.pi)
        
        # Hyperbolic tangent and polynomial mixing with higher-order terms
        mix_term = 0
        for i in range(self.dim):
            mix_term += np.tanh(x_norm[i]**4) * (x_norm[i]**8 - 2*x_norm[i]**6 + x_norm[i]**4)
        
        # Cross-dimensional chaotic coupling with exponential weights and rotational components
        chaos_term = 0
        for i in range(self.dim):
            weight = np.exp(-i / self.dim) * np.sin(i * np.pi / 4)
            for j in range(i+1, self.dim):
                if j < self.dim:
                    # Add rotational symmetry component
                    rot_component = np.sin(x_norm[i] * x_norm[j] + np.pi/4) * np.cos(x_norm[i] + x_norm[j])
                    chaos_term += weight * rot_component * np.exp(-np.abs(x_norm[i] - x_norm[j]))
        
        # Quaternion-inspired rotational coupling terms
        quat_term = 0
        for i in range(0, self.dim, 2):
            if i+1 < self.dim:
                quat_term += np.sin(x_norm[i]**2 + x_norm[i+1]**2) * np.cos(x_norm[i] * x_norm[i+1])
        
        # Combine all terms with dynamic scaling
        result = 0.3 * rbf_sum + 0.25 * sine_mod + 0.18 * fractal_term + \
                 0.22 * mix_term + 0.05 * chaos_term + 0.05 * quat_term
        
        # Add conditioning and noise to increase difficulty
        conditioning = 0.03 * np.sum(x_norm**10)
        noise = 0.01 * np.random.random()
        
        return result + conditioning + noise