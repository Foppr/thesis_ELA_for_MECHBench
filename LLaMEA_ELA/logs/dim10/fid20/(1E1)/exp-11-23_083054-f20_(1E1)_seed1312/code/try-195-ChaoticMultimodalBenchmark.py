import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Slightly modified chaotic parameters for increased complexity
        self.chaos_params = np.array([np.sin(i * 0.71) * 0.62 + 0.82 for i in range(dim)])
        self.saddle_points = np.array([np.cos(i * 0.51) * 1.82 for i in range(dim)])
        
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
        
        # Asymmetric correlation terms with modified interaction strengths
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                corr_strength = 0.92 + 0.52 * np.sin(0.6 * (i + j)) * self.chaos_params[i] * self.chaos_params[j]
                asymmetry = 1.22 + 0.42 * np.cos(0.8 * (x_norm[i] - x_norm[j]))
                f3 += corr_strength * x_norm[i] * x_norm[j] * asymmetry
        
        # Mixed exponential and trigonometric component with modified scaling
        f4 = 0.0
        for i in range(self.dim):
            exp_factor = np.exp(-0.15 * np.abs(x_norm[i]))
            trig_factor = np.sin(2.5 * x_norm[i]) + 0.6 * np.cos(3.5 * x_norm[i])
            f4 += exp_factor * trig_factor * (1.22 + 0.32 * np.sin(0.9 * i))
        
        # Enhanced non-smoothness with sharper gradients
        f5 = 0.0
        for i in range(self.dim):
            sharpness = 1.22 + 0.62 * np.sin(1.3 * i)
            f5 += sharpness * np.abs(x_norm[i])**1.92 * np.exp(-0.05 * x_norm[i]**2)
        
        # Combine with dynamic weights
        weights = [0.25 + 0.04 * np.sin(0.7 * i) for i in range(5)]
        
        return weights[0] * f1 + weights[1] * f2 + weights[2] * f3 + weights[3] * f4 + weights[4] * f5