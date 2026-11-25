import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for each dimension
        self.chaos_params = np.array([np.sin(i * 0.7) * 0.6 + 0.8 for i in range(dim)])
        self.saddle_points = np.array([np.cos(i * 0.5) * 1.8 for i in range(dim)])
        # Additional chaotic parameters for increased complexity
        self.freq_modulators = np.array([np.sin(i * 0.3) * 0.4 + 0.6 for i in range(dim)])
        self.amp_modulators = np.array([np.cos(i * 0.4) * 0.3 + 0.7 for i in range(dim)])
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Highly oscillatory chaotic component with dynamic frequencies and amplitudes
        f1 = 0.0
        for i in range(self.dim):
            freq = 8.0 + 3.0 * np.sin(0.5 * i) * self.freq_modulators[i]
            amp = 3.0 + 2.0 * np.sin(0.7 * i) * self.amp_modulators[i]
            f1 += amp * np.sin(freq * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2)
        
        # Enhanced polynomial potential with multiple saddle points and higher-order terms
        f2 = 0.0
        for i in range(self.dim):
            saddle = self.saddle_points[i]
            poly_term = (x_norm[i] - saddle)**7 + 0.8 * (x_norm[i] - saddle)**6 + 0.5 * (x_norm[i] - saddle)**5
            f2 += poly_term * np.exp(-0.3 * (x_norm[i] - saddle)**2)
        
        # Dynamic correlation terms with time-varying interaction strengths
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                corr_strength = 1.5 + 0.8 * np.sin(0.6 * (i + j)) * self.chaos_params[i] * self.chaos_params[j]
                asymmetry = 1.5 + 0.5 * np.cos(0.9 * (x_norm[i] - x_norm[j]))
                f3 += corr_strength * x_norm[i] * x_norm[j] * asymmetry * np.sin(0.3 * (i + j))
        
        # Mixed exponential and trigonometric component with chaotic scaling and phase shifts
        f4 = 0.0
        for i in range(self.dim):
            exp_factor = np.exp(-0.2 * np.abs(x_norm[i]))
            trig_factor = np.sin(3.0 * x_norm[i]) + 0.7 * np.cos(4.0 * x_norm[i]) + 0.3 * np.sin(5.0 * x_norm[i])
            phase_shift = 0.5 * np.cos(0.8 * i)
            f4 += exp_factor * trig_factor * (1.5 + 0.4 * np.sin(1.2 * i) + phase_shift)
        
        # Enhanced non-smoothness with sharper gradients and multiple discontinuity points
        f5 = 0.0
        for i in range(self.dim):
            sharpness = 1.5 + 0.8 * np.sin(1.5 * i)
            f5 += sharpness * np.abs(x_norm[i])**2.1 * np.exp(-0.1 * x_norm[i]**2) + \
                   0.5 * np.sin(5.0 * x_norm[i]) * np.cos(3.0 * x_norm[i])
        
        # Additional chaotic noise component
        f6 = 0.0
        for i in range(self.dim):
            noise_amp = 0.2 + 0.1 * np.sin(0.9 * i)
            f6 += noise_amp * np.sin(10.0 * x_norm[i]) * np.exp(-0.05 * x_norm[i]**2)
        
        # Combine with dynamic weights
        weights = [0.2 + 0.03 * np.sin(0.7 * i) for i in range(6)]
        
        return weights[0] * f1 + weights[1] * f2 + weights[2] * f3 + weights[3] * f4 + weights[4] * f5 + weights[5] * f6