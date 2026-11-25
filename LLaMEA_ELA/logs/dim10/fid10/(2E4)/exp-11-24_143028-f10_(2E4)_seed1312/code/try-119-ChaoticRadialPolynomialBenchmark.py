import numpy as np

class ChaoticRadialPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with exponential decay
        result = 0.5 * np.sum(x**2) * np.exp(-0.1 * np.sum(x**2))
        
        # Chaotic sine-wave modulations with varying frequencies
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += np.sin(13 * x[i]) * np.cos(11 * x[i]) * np.sin(7 * x[i])
        result += 2.5 * chaos_term
        
        # Radial basis functions with dynamic widths and phase shifts
        rbf_sum = 0.0
        centers = [-4.0, -2.0, 0.0, 2.0, 4.0]
        for center in centers:
            rbf_sum += np.exp(-0.5 * np.sum((x - center)**2))
        result += 1.8 * rbf_sum
        
        # Polynomial coupling with cross-dimensional interactions
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_coupling += (x[i]**2 + x[j]**2) * np.sin(5 * (x[i] - x[j]))
        result += 0.8 * poly_coupling
        
        # Asymmetric boundary effects with logarithmic penalties
        boundary_penalty = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                boundary_penalty += 1.5 * np.log(1 + np.abs(x[i]))
            else:
                boundary_penalty += 2.0 * np.log(1 + x[i])
        result += 0.7 * boundary_penalty
        
        # High-frequency trigonometric oscillations
        freq_osc = 0.0
        for i in range(self.dim):
            freq_osc += np.sin(30 * x[i]) * np.cos(25 * x[i]) + np.sin(28 * x[i])
        result += 1.2 * freq_osc
        
        # Cross-dimensional exponential coupling with cosine modulation
        exp_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_coupling += np.exp(-0.3 * (x[i] - x[j])**2) * np.cos(8 * (x[i] + x[j]))
        result += 0.9 * exp_coupling
        
        # Multimodal structure with multiple local optima
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 1.5 * np.sin(20 * x[i]) * np.cos(15 * x[i]) + 0.8 * np.sin(35 * x[i])
        result += 1.4 * multimodal
        
        # Weighted sum of polynomial and trigonometric components
        poly_trig = 0.0
        for i in range(self.dim):
            poly_trig += (x[i]**3 + 0.5 * x[i]**2 - 0.3 * x[i]) * np.sin(10 * x[i])
        result += 1.1 * poly_trig
        
        # Additional chaotic modulation with hyperbolic tangent
        tanh_mod = 0.0
        for i in range(self.dim):
            tanh_mod += np.tanh(12 * x[i]) * np.sin(18 * x[i])
        result += 0.6 * tanh_mod
        
        # Fractal-like structure with recursive sine components
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(30 * x[i]) * np.sin(25 * x[i]) * np.cos(20 * x[i])
        result += 1.3 * fractal
        
        return result