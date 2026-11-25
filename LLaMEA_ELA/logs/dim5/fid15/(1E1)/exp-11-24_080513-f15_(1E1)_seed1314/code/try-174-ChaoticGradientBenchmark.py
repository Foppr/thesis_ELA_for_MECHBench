import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced chaotic component with dynamic scaling and multi-seed logistic maps
        chaotic = 0.0
        r_values = [3.5, 3.7, 3.9, 4.0]
        for i in range(self.dim):
            x_prev = 0.5
            r_idx = i % len(r_values)
            r = r_values[r_idx]
            for _ in range(20):  # More iterations for stronger chaos
                x_prev = r * x_prev * (1 - x_prev)
            chaotic += np.sin(x_normalized[i] * x_prev * 15) * np.cos(x_normalized[i] * x_prev * 10)
        
        # Enhanced gradient-based component with dynamic conditioning and polynomial terms
        gradient = 0.0
        for i in range(self.dim):
            condition = 1.0 + 5.0 * np.sin(i * 0.5) * np.cos(i * 0.3)
            poly_term = x_normalized[i]**4 + 0.5 * x_normalized[i]**3 + 0.2 * x_normalized[i]**2
            gradient += condition * poly_term * np.exp(-0.5 * x_normalized[i]**2)
        
        # Enhanced saddle point region with coupled hyperbolic tangent and cubic interactions
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended coupling
                coupling = np.tanh(x_normalized[i]) * np.tanh(x_normalized[j])
                diff_term = (x_normalized[i] - x_normalized[j])**3
                saddle += coupling * diff_term
        
        # Discontinuous region with enhanced step function and multi-frequency sinusoidal modulation
        discontinuous = 0.0
        for i in range(self.dim):
            step_val = 1.0 if x_normalized[i] > 0 else -1.0
            freq_mod = np.sin(8 * x_normalized[i]) * np.cos(6 * x_normalized[i])
            discontinuous += step_val * freq_mod * np.exp(-np.abs(x_normalized[i]))
        
        # Enhanced multi-scale harmonic interaction with adaptive weights and phase shifts
        harmonic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_normalized[i] - x_normalized[j])
                weight = np.exp(-dist * 5.0) * (1 + 0.5 * np.sin(dist * 3))
                phase_shift = np.pi / 4
                harmonic += weight * np.sin(4 * (x_normalized[i] + x_normalized[j]) + phase_shift) * np.cos(4 * (x_normalized[i] - x_normalized[j]) + phase_shift)
        
        # Additional nonlinearity with higher-order terms and modified sinusoidal scaling
        nonlin = 0.0
        for i in range(self.dim):
            nonlin += (x_normalized[i]**5) * np.sin(x_normalized[i])**3 + 0.3 * (x_normalized[i]**4) * np.cos(x_normalized[i])
        
        # Combined fitness with adaptive scaling and added noise resistance
        return (0.25 * chaotic + 0.3 * gradient + 0.18 * saddle + 
                0.17 * discontinuous + 0.08 * harmonic + 0.02 * nonlin)