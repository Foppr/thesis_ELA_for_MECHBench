import numpy as np

class ExponentialTrigonometricValley:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay components with varying rates
        exp_decay = 0
        for i in range(self.dim):
            rate = 0.1 + 0.4 * np.sin(i * 0.6) + 0.2 * np.cos(i * 0.3)
            exp_decay += np.exp(-rate * np.abs(x[i])) * np.sin(i * x[i])
        
        # Trigonometric wave interference with dynamic amplitudes
        wave_interference = 0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(i * 0.8)
            wave_interference += amp * np.sin(x[i] * (1.0 + 0.3 * np.cos(i * 0.5))) * np.cos(x[i] * (0.5 + 0.2 * np.sin(i * 0.7)))
        
        # Adaptive parabolic valleys with dynamic curvature
        parabolic_valleys = 0
        for i in range(self.dim):
            curvature = 0.5 + 0.5 * np.sin(i * 0.4)
            valley_center = -3.0 + 6.0 * (i / max(1, self.dim - 1)) + 0.3 * np.cos(i * 0.9)
            parabolic_valleys += curvature * (x[i] - valley_center)**2
        
        # Dynamic conditioning with chaotic scaling factors
        conditioning = 0
        for i in range(self.dim):
            scale = 1.0 + 0.8 * np.sin(i * 0.5) + 0.3 * np.cos(i * 0.2)
            conditioning += scale * x[i]**2
        
        # Saddle-point distribution with chaotic positioning
        saddle_points = 0
        for i in range(self.dim - 1):
            pos = -4.0 + 8.0 * (i / max(1, self.dim - 1)) + 0.4 * np.sin(i * 0.7)
            saddle_points += (x[i] - pos) * (x[i+1] - pos) * np.sin(i * 0.3)
        
        # Global oscillation modulation
        global_osc = np.sin(0.2 * np.sum(x**2)) * np.cos(0.1 * np.sum(x)) * np.exp(-0.05 * np.sum(np.abs(x)))
        
        # Add noise-like chaotic perturbations
        chaos_perturb = 0
        for i in range(self.dim):
            perturb = 0.1 * np.sin(x[i] * (2.0 + 0.5 * np.cos(i * 0.4)))
            chaos_perturb += perturb
        
        # Combine all components with refined weights
        return 1.5 * exp_decay + 1.2 * wave_interference + 0.8 * parabolic_valleys + 0.6 * conditioning + 0.4 * saddle_points + 0.2 * global_osc + 0.1 * chaos_perturb