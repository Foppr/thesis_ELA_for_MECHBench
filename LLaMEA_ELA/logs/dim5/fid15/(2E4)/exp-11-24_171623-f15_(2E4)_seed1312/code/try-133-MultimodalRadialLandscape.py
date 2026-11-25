import numpy as np

class MultimodalRadialLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial basis function components with chaotic modulation
        rbf_sum = 0.0
        centers = np.linspace(-1, 1, min(7, self.dim))
        for i in range(self.dim):
            center_idx = i % len(centers)
            center = centers[center_idx]
            distance = np.abs(x_norm[i] - center)
            # Add chaotic modulation to RBF
            chaos_mod = 1.0 + 0.2 * np.sin(15 * x_norm[i])
            rbf_sum += np.exp(-3.0 * distance**2) * np.sin(8 * x_norm[i]) * chaos_mod
        
        # Enhanced cross-dimensional interaction terms with dynamic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction scope
                distance = np.abs(x_norm[i] - x_norm[j])
                # Dynamic coupling based on both dimensions
                coupling = (1 + 0.3 * np.sin(x_norm[i] * x_norm[j] * 10.0) + 
                           0.2 * np.cos(x_norm[i] + x_norm[j]))
                cross_term += coupling * np.exp(-distance * 4.0) * (x_norm[i]**2 + x_norm[j]**2)
        
        # Multi-frequency sinusoidal oscillations with adaptive amplitudes and phase shifts
        sin_sum = 0.0
        frequencies = [1.0, 2.5, 5.0, 8.0, 13.0]
        phases = [0.0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]
        for i in range(self.dim):
            freq_idx = i % len(frequencies)
            freq = frequencies[freq_idx]
            phase = phases[freq_idx]
            sin_sum += np.sin(x_norm[i] * freq * np.pi + phase) * np.cos(x_norm[i] * freq * np.pi / 2.0 + phase)
        
        # Saddle-point like behavior with enhanced hyperbolic tangent conditioning
        saddle_sum = 0.0
        for i in range(self.dim):
            # More complex saddle structure
            saddle_sum += (np.tanh(x_norm[i]) ** 3) * (x_norm[i]**4 - 4 * x_norm[i]**2 + 3)
        
        # Enhanced chaotic modulation with dynamic scaling
        chaos_factor = 1.0 + 0.4 * np.sin(np.sum(x_norm**2) * 7.0) * np.cos(np.sum(x_norm) * 3.0)
        
        # Combine all terms with adjusted weighting for better balance
        result = 0.25 * rbf_sum + 0.3 * cross_term + 0.2 * sin_sum + 0.25 * saddle_sum
        
        # Add adaptive penalty term to improve fitness score
        penalty = 0.1 * np.sum(np.abs(x_norm)**3)
        
        return (result * chaos_factor + penalty) * (1 + 0.15 * np.sum(np.abs(x_norm)))