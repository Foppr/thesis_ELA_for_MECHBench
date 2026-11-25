import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for each dimension
        self.chaos_params = np.array([np.sin(i * 0.8) * 0.5 + 0.7 for i in range(dim)])
        self.saddle_points = np.array([np.cos(i * 0.6) * 2.0 for i in range(dim)])
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Chaotic sinusoidal component with varying frequencies and amplitudes
        f1 = 0.0
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(0.4 * i) + 0.5 * np.cos(0.3 * i)
            amp = 1.5 + 0.8 * np.sin(0.6 * i) + 0.3 * np.cos(0.5 * i)
            f1 += amp * np.sin(freq * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2)
        
        # Polynomial potential with asymmetric saddle points
        f2 = 0.0
        for i in range(self.dim):
            saddle = self.saddle_points[i]
            poly_term = (x_norm[i] - saddle)**4 + 0.5 * (x_norm[i] - saddle)**3
            f2 += poly_term * np.exp(-0.3 * (x_norm[i] - saddle)**2)
        
        # Asymmetric correlation terms with chaotic interaction strengths
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                corr_strength = 0.8 + 0.4 * np.sin(0.5 * (i + j)) * self.chaos_params[i] * self.chaos_params[j]
                asymmetry = 1.0 + 0.3 * np.cos(0.7 * (x_norm[i] - x_norm[j]))
                f3 += corr_strength * x_norm[i] * x_norm[j] * asymmetry
        
        # Mixed exponential and trigonometric component with chaotic scaling
        f4 = 0.0
        for i in range(self.dim):
            exp_factor = np.exp(-0.2 * np.abs(x_norm[i]))
            trig_factor = np.sin(2.0 * x_norm[i]) + 0.5 * np.cos(3.0 * x_norm[i])
            f4 += exp_factor * trig_factor * (1.0 + 0.2 * np.sin(0.8 * i))
        
        # Combine with dynamic weights
        weights = [0.25 + 0.05 * np.sin(0.6 * i) for i in range(4)]
        
        return weights[0] * f1 + weights[1] * f2 + weights[2] * f3 + weights[3] * f4