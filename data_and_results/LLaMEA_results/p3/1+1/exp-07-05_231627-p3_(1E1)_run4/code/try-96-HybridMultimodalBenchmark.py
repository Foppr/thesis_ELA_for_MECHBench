import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # Exponential decay components with varying rates and orientations
        exp_decay = np.sum(np.exp(-5 * np.abs(x_norm)) * np.exp(-3 * np.abs(x_norm**2)) + 
                          np.exp(-7 * np.abs(x_norm**3)) * np.exp(-2 * np.abs(x_norm**4)))
        
        # Trigonometric wave interference with adaptive frequencies and amplitudes
        wave_freq = 10 + 5 * np.sin(0.5 * np.sum(x_norm))
        wave_amp = 2.0 + 1.5 * np.cos(0.3 * np.sum(x_norm**2))
        wave_interference = np.sum(wave_amp * np.sin(wave_freq * x_norm) * np.cos(wave_freq * x_norm**2))
        
        # Adaptive parabolic valleys with dynamic curvature and position
        valleys = 0
        for i in range(min(5, self.dim)):
            curvature = 2.0 + 3.0 * np.sin(0.2 * i * np.sum(x_norm))
            position = 0.5 * np.sin(0.1 * i * np.sum(x_norm))
            valleys += curvature * (x_norm[i] - position)**2
        
        # Gaussian peak superposition with dynamic scaling and shifting
        peaks = 0
        for i in range(8):
            scale = 1.0 + 0.5 * np.sin(0.3 * i * np.sum(x_norm))
            shift = 0.3 * np.cos(0.2 * i * np.sum(x_norm))
            peaks += scale * np.exp(-5 * (x_norm - shift)**2)
        
        # Cross-dimensional coupling with directional bias and nonlinearity
        cross_coupling = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                cross_coupling += (x_norm[i]**2 + x_norm[i+1]**2) * np.sin(5 * (x_norm[i] - x_norm[i+1]))
        
        # Fractional polynomial with varying exponents and adaptive weights
        fractional_poly = np.sum((x_norm**3.5 + 0.5 * x_norm**2.8 + 0.3 * x_norm**1.9)**2)
        
        # Combine all components with dynamic weighting based on input characteristics
        weight_exp = 0.25 + 0.1 * np.sin(0.5 * np.sum(x_norm**2))
        weight_wave = 0.3 + 0.15 * np.cos(0.3 * np.sum(x_norm))
        weight_valley = 0.2 + 0.1 * np.sin(0.4 * np.sum(x_norm**3))
        weight_peak = 0.15 + 0.05 * np.cos(0.2 * np.sum(x_norm))
        weight_cross = 0.1 + 0.05 * np.sin(0.6 * np.sum(x_norm))
        weight_frac = 0.05 + 0.02 * np.cos(0.1 * np.sum(x_norm))
        
        result = (weight_exp * exp_decay + 
                 weight_wave * wave_interference + 
                 weight_valley * valleys + 
                 weight_peak * peaks + 
                 weight_cross * cross_coupling + 
                 weight_frac * fractional_poly)
        
        # Add dynamic noise that scales with input magnitude
        noise = 0.02 * (1 + 0.5 * np.abs(np.sum(x_norm**3))) * np.random.uniform(-1, 1)
        
        return result + noise