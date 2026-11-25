import numpy as np

class FractalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Fractal-like self-similar structure with recursive scaling
        fractal = np.sum(np.power(np.abs(x_scaled), 1.7) * 
                        np.sin(20.0 * np.power(np.abs(x_scaled), 0.6)) + 
                        0.5 * np.power(np.abs(x_scaled), 2.3) * 
                        np.cos(15.0 * np.power(np.abs(x_scaled), 0.8)))
        
        # Chaotic sine-wave interactions with varying amplitudes and frequencies
        chaotic = np.sum(np.sin(30.0 * x_scaled + np.sin(25.0 * x_scaled)) * 
                        np.cos(22.0 * x_scaled + np.cos(18.0 * x_scaled)) + 
                        0.7 * np.sin(40.0 * x_scaled**2 + np.sin(35.0 * x_scaled**2)) * 
                        np.cos(32.0 * x_scaled**2 + np.cos(28.0 * x_scaled**2)))
        
        # Dynamic conditioning with exponential and logarithmic scaling
        cond = np.sum(np.exp(2.0 * np.abs(x_scaled)) * np.log(1.0 + 3.0 * np.abs(x_scaled)) + 
                     0.6 * np.exp(-1.5 * x_scaled**2) * np.log(1.0 + 2.0 * x_scaled**2))
        
        # Cross-dimensional coupling with fractional polynomial interactions
        cross = np.sum((x_scaled[:-1]**1.5 + x_scaled[1:]**1.5) * 
                     np.sin(5.0 * (x_scaled[:-1] - x_scaled[1:])) + 
                     0.8 * (x_scaled[:-2]**2.5 + x_scaled[2:]**2.5) * 
                     np.cos(3.0 * (x_scaled[:-2] + x_scaled[2:])))
        
        # Resonance peaks with varying widths and heights
        resonance = np.sum(1.5 * np.exp(-8.0 * (x_scaled - 0.2)**2) * 
                         np.sin(12.0 * x_scaled) + 
                         0.9 * np.exp(-6.0 * (x_scaled + 0.3)**2) * 
                         np.cos(15.0 * x_scaled) + 
                         0.4 * np.exp(-10.0 * (x_scaled - 0.7)**2) * 
                         np.sin(18.0 * x_scaled))
        
        # Asymmetric basin with weighted sum of components
        return 0.25 * fractal + 0.3 * chaotic + 0.15 * cond + 0.2 * cross + 0.1 * resonance + 1.4