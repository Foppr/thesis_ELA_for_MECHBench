import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for each dimension
        self.chaos_params = np.array([np.sin(i * 0.7) * 0.6 + 0.8 for i in range(dim)])
        self.saddle_points = np.array([np.cos(i * 0.5) * 1.8 for i in range(dim)])
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Chaotic sinusoidal component with varying frequencies and amplitudes
        f1 = 0.0
        for i in range(self.dim):
            freq = 4.0 + 1.5 * np.sin(0.5 * i) + 0.7 * np.cos(0.4 * i)
            amp = 2.0 + 1.0 * np.sin(0.7 * i) + 0.5 * np.cos(0.6 * i)
            f1 += amp * np.sin(freq * x_norm[i]) * np.exp(-0.3 * x_norm[i]**2)
        
        # Polynomial potential with asymmetric saddle points
        f2 = 0.0
        for i in range(self.dim):
            saddle = self.saddle_points[i]
            poly_term = (x_norm[i] - saddle)**5 + 0.7 * (x_norm[i] - saddle)**4
            f2 += poly_term * np.exp(-0.2 * (x_norm[i] - saddle)**2)
        
        # Asymmetric correlation terms with chaotic interaction strengths
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                corr_strength = 0.9 + 0.5 * np.sin(0.6 * (i + j)) * self.chaos_params[i] * self.chaos_params[j]
                asymmetry = 1.2 + 0.4 * np.cos(0.8 * (x_norm[i] - x_norm[j]))
                f3 += corr_strength * x_norm[i] * x_norm[j] * asymmetry
        
        # Mixed exponential and trigonometric component with chaotic scaling
        f4 = 0.0
        for i in range(self.dim):
            exp_factor = np.exp(-0.15 * np.abs(x_norm[i]))
            trig_factor = np.sin(2.5 * x_norm[i]) + 0.6 * np.cos(3.5 * x_norm[i])
            f4 += exp_factor * trig_factor * (1.2 + 0.3 * np.sin(0.9 * i))
        
        # Add enhanced non-smoothness with sharper gradients
        f5 = 0.0
        for i in range(self.dim):
            # Introduce more abrupt changes
            sharpness = 1.2 + 0.6 * np.sin(1.3 * i)
            f5 += sharpness * np.abs(x_norm[i])**1.9 * np.exp(-0.05 * x_norm[i]**2)
        
        # Combine with dynamic weights
        weights = [0.25 + 0.04 * np.sin(0.7 * i) for i in range(5)]
        
        return weights[0] * f1 + weights[1] * f2 + weights[2] * f3 + weights[3] * f4 + weights[4] * f5